class CFPBDownloadError(Exception):
    """Raised when CFPB data download fails."""
    pass


class ValidationError(Exception):
    """Raised when data validation fails."""
    pass


class S3UploadError(Exception):
    """Raised when S3 upload fails."""
    pass
