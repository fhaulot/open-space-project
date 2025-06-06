

class Openspace(self, tables, number_of_tables):

    def __init__(self, tables):
        self.tables = tables
        self.number_of_tables = len(tables)

    
    def organize(self, names):
         
         random.shuffle(names)

         for n in names:
              for t in self.number_of_tables:
                   if Table.has_free_spot(t):
                       self.seat(n)
  


    def display():
        for num, table in enumerate(self.tables, start=1):
            print(f"Table {num}:")
            for seat in table.seats:
                attendant = seat.attendant
                print(f"\n{attendantt}")
            print("\n")

    def store(filename):
            data = []
            
            for num, table in enumerate(self.tables, start=1):
                for seat in table.seats:  
                     data.append(
                          f"Table {num} ",
                          seat.attendant 
                     )
            
            df = pd.DataFrame(data)
            df.to_excel(fileName, index=False)