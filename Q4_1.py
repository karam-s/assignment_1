class the_Country:
    def __init__(self,Country="",Capital="",area=0,Population=0):
        self._Country=Country
        self._Capital=Capital
        self._area=area
        self._Population=Population
    def getCountry(self):
        return self._Country
    def getCapital(self):
        return self._Capital
    def getarea(self):
        return self._area
    def getPopulation(self):
        return self._Population
    def setPopulation(self,Population):
        self._Population=Population
    def __str__(self):
        return "The Country: "+self._Country +"\n"+"The Capital: "+self._Capital


class Capital_p(the_Country):
    def __init__(self,Country="",Capital="",area=0,Population=0,Population_in_Capital=0):
        super().__init__(Country,Capital,area,Population)
        self._Population_in_Capital=Population_in_Capital
    def percent(self):
        per =(100*self._Population_in_Capital)/self._Population
        return per
    def __str__(self):
        return "The number of inhabitants in the capital is equal to \
"+str(self.percent())+"% Of the Country's total population"

class Capital_a(the_Country):
    def __init__(self,Country="",Capital="",area=0,Population=0,area_C=0):
        super().__init__(Country,Capital,area,Population)
        self._area_C=area_C
    def percent(self):
        per =(100*self._area_C)/self._area
        return "The area of ​​the capital is about "+str(per)+"% of the total area of ​​the country"
    
