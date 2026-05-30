SELECT *
FROM @risk_complaints_stage
(
    FILE_FORMAT => 'COMPLAINTS_CSV_FORMAT'
)
LIMIT 5;
