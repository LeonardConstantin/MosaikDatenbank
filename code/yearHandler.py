from pprint import pprint

class yearHandler:
    def __init__(self):
        self.daten=[]
        self.generate_all_years(False)

    def handle_delete(self,value):
        value=str(value).strip()
        if  len(value)==9:
            left=value[0:4]
            right=value[5:9]
            mid=value[4:5]
            if mid=="-" and self.check_valid_number(left) and self.check_valid_number(right):
                self.set_daten(self.delete_years([int(left),int(right)]))
        elif len(value)==4:
            if self.check_valid_number(value):
                self.set_daten(self.delete_year(int(value)))
        else:
            print("Falsches Format")
            return [None]

    def handle_add(self,value):
        value=str(value).strip()
        if  len(value)==9:
            left=value[0:4]
            right=value[5:9]
            mid=value[4:5]
            if mid=="-" and self.check_valid_number(left) and self.check_valid_number(right):
                self.set_daten(self.add_years([int(left),int(right)]))
        elif len(value)==4:
            if self.check_valid_number(value):
                self.set_daten(self.add_year(int(value)))
        else:
            print("Falsches Format")
            return [None]

    def check_valid_number(self,value):
        try:
            int(value)
            return True
        except:
            return False

    def generate_all_years(self,testing):
        if testing:
            for years in range(0,63):
                if years %2==0:
                    self.daten.append(1960+years)
        else:
            for years in range(0,63):
                self.daten.append(1960+years)

    def delete_years(self,values):
        new_daten=[]
        for year in self.daten:
            if year>=values[0] and year<=values[1]:
                pass
            else:
                new_daten.append(year)
        return new_daten

    def delete_year(self,value):
        new_daten=[]
        for year in self.daten:
            if year!=value:
                new_daten.append(year)
        #print(new_daten)
        return new_daten

    def add_year(self,value):
        new_daten=[]
        i=0
        while self.daten[i]<value and i<len(self.daten):
            new_daten.append(self.daten[i])
            i=i+1
        if i!=len(self.daten):
            if self.daten[i]!=value:
                new_daten.append(value)
            for y in range(i,len(self.daten)):
                new_daten.append(self.daten[y])    
        else:
            for y in range(i,len(self.daten)):
                new_daten.append(self.daten[y])  
        return new_daten

    def add_years(self,values):
        new_daten=self.daten.copy()
        for y in range(values[0],values[1]):
            new_daten.append(y)
        return new_daten

    def get_daten(self):
        return self.daten

    def get_years_formated(self):
        #Was wenn Index leer?
        index=[]
        for y in range(0,len(self.daten)-1):
            #print(self.daten[y]+1, self.daten[y+1])
            if self.daten[y]+1!=self.daten[y+1]:
                print(self.daten[y]+1, self.daten[y+1])
                index.append(y)
        print(index)
        if len(index)==0:
            return self.get_min_max_years([self.daten])
        else:
            return self.get_min_max_years(self.get_date_parts(index))
    
    def get_min_max_years(self,year_lists):
        min_max_list=[]
        for interval in year_lists:
            min_max_list.append(str(interval[0])+"-"+str(interval[-1]))
        return min_max_list

    def get_date_parts(self,index):
        liste=[]
        liste.append(self.daten[0:index[0]+1])
        for i in range(1,len(index)):  
            liste.append(self.daten[index[i-1]+1:index[i]+1])
        liste.append(self.daten[index[-1]+1:])
        return liste

    def set_daten(self,daten):
        self.daten=daten

