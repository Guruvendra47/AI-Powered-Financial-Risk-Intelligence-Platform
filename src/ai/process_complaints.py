from datetime import datetime

from src.cloud.snowflake.snowflake_connection import (
    get_connection
)

from src.ai.complaint_analyzer import (
    analyze_complaint
)

from src.ingestion.utils.logger import (
    get_logger
)

logger = get_logger(__name__)


def process_complaints():

    conn = get_connection()

    cursor = conn.cursor()

    try:

        logger.info(
            "Reading unprocessed complaints..."
        )

        cursor.execute(
            """
            SELECT
                f.complaint_id,
                f.consumer_complaint_narrative

            FROM ANALYTICS_GOLD.FACT_COMPLAINTS f

            LEFT JOIN ANALYTICS_GOLD.RISK_ANALYSIS r
                ON f.complaint_id = r.complaint_id

            WHERE r.complaint_id IS NULL
            AND f.consumer_complaint_narrative IS NOT NULL

            LIMIT 100
            """
        )

        complaints = cursor.fetchall()

        logger.info(
            f"Found {len(complaints)} complaints"
        )

        for complaint_id, narrative in complaints:

            try:

                result = analyze_complaint(
                    narrative
                )

                cursor.execute(
                    """
                    INSERT INTO
                    ANALYTICS_GOLD.RISK_ANALYSIS
                    (
                        complaint_id,
                        risk_category,
                        sentiment,
                        complaint_summary,
                        analysis_status,
                        model_name,
                        processed_timestamp
                    )
                    VALUES
                    (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                    )
                    """,
                    (
                        complaint_id,
                        result["risk_category"],
                        result["sentiment"],
                        result["summary"],
                        "SUCCESS",
                        "gpt-4.1-mini",
                        datetime.utcnow()
                    )
                )

            except Exception as e:

                logger.error(
                    f"Failed complaint "
                    f"{complaint_id}: {e}"
                )

        conn.commit()

        logger.info(
            "AI enrichment completed."
        )

    finally:

        cursor.close()
        conn.close()


if __name__ == "__main__":

    process_complaints()