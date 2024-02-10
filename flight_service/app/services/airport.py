from sqlalchemy.orm import Session

from models.airport import AirportModel
from schemas.airport import AirportCreate
from exceptions.http_exceptions import NotFoundException, ConflictException
from cruds.interfaces.airport import IAirportCRUD


class AirportService():
    def __init__(self, airportCRUD: type[IAirportCRUD], db: Session):
        self._airportCRUD = airportCRUD(db)
        
    async def get_all(
            self,
            page: int = 1,
            size: int = 100
        ):
        return await self._airportCRUD.get_all(
                offset=(page - 1) * size, 
                limit=size
            )

    async def get_by_id(self, airport_id: int):
        airport = await self._airportCRUD.get_by_id(airport_id)
        if airport == None:
            raise NotFoundException(prefix="Get airport")
        
        return airport
    
    async def add(self, airport_create: AirportCreate):
        airport = AirportModel(**airport_create.model_dump())
        airport = await self._airportCRUD.add(airport)
        if airport == None:
            raise ConflictException(prefix="Add airport")
        
        return airport
    
    async def delete(self, airport_id: int):
        airport = await self._airportCRUD.get_by_id(airport_id)
        if airport == None:
            raise NotFoundException(prefix="Delete airport")
        
        return await self._airportCRUD.delete(airport)
