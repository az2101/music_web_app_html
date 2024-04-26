class AlbumParametersValidator:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def is_valid(self):
        return self._is_title_valid() and self._is_year_valid()
    
    def generate_errors(self):
        errors = []
        if not self._is_title_valid():
            errors.append("Title can't be blank")
        if not self._is_year_valid():
            errors.append("Year can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ', '.join(errors)
    
    def get_valid_title(self):
        if not self._is_title_valid():
            raise ValueError("Cannot get valid title")
        return self.title
    
    def get_valid_year(self):
        if not self._is_year_valid():
            raise ValueError("Cannot get valid Release Year")
        return int(self.year)
    
    def _is_title_valid(self):
        if self.title is None:
            return False
        if self.title =='':
            return False
        return True
    
    def _is_year_valid(self):
        if self.year == None:
            return False
        if not self.year.isdigit():
            return False
        return True
    