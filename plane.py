class Plane:
    def __init__(self, flight_code: str, plane_type: str) -> None:
        """Initialize a Plane object.

        Args:
            flight_code (str): The flight code of the plane.
            plane_type (str): The type of the plane ('landing', 'takeoff', or 'emergency').

        """
        self._flight_code: str = flight_code
        self._plane_type: str = plane_type

    @property
    def flight_code(self) -> str:
        return self._flight_code
    
    @flight_code.setter
    def flight_code(self, code: str) -> None:
        self._flight_code = code

    @property
    def plane_type(self) -> str:
        return self._plane_type
    
    @plane_type.setter
    def plane_type(self, type: str) -> None:
        self._plane_type = type

    def __repr__(self) -> str:
        if self.plane_type == "emergency":
            return f" Plane flight_code: \033[93m{self.flight_code}\033[0m, plane_type: \033[91m{self.plane_type}\033[0m"
        else:
            return f" Plane flight_code: \033[93m{self.flight_code}\033[0m, plane_type: \033[93m{self.plane_type}\033[0m"
    