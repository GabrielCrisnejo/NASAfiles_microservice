from pydantic import BaseModel, Field

class DownloadRequest(BaseModel):
    base_url: str = Field(..., description="Base URL to download the products", examples=["https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Ancillary/GLOBAL"])
    filter_list: list = Field(..., description="List of products to download", examples=[["GMAO_MERRA2.20230628T100000.MET.nc"]])
    filter_date: str = Field(..., description="Date to download the products", examples=['20230628'])