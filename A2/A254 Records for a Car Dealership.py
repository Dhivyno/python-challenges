class CarRecord():
   def __init__(self, VehicleID, Registration, DateOfRegistration, EngineSize, PurchasePrice):
      self.VehicleID = VehicleID
      self.Registration = Registration
      self.DateofRegistration = DateOfRegistration
      self.EngineSize = EngineSize
      self.PurchasePrice = PurchasePrice

CarRecord.VehicleID = "123864"
CarRecord.Registration = "Bob Tim"
CarRecord.DateofRegistration = "20/10/2004"
CarRecord.EngineSize = "2000cc"
CarRecord.PurchasePrice = "$300,000"

array = [CarRecord.VehicleID, CarRecord.Registration, CarRecord.DateofRegistration, CarRecord.EngineSize, CarRecord.PurchasePrice]
print(array)
