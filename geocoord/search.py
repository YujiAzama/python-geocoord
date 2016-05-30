from geocoord import locations_repo as lr


class Search(object):

    def __init__(self):
        self.repo = lr.LocationsRepository()

    def find_coord_by_city(self, keyword):
        return self.repo.get_cities(keyword)

    def find_city_by_coord(self, lat, lon):
        pass


if __name__ == "__main__":
    search = Search()
    print search.find_coord_by_city("tokyo")
