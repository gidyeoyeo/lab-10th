def main():
    display_main_menu()
    all_temps=get_user_input()
    average_temps=calc_average_temperature(all_temps)
    help_sort=sorted_temps(all_temps)
    min_max=calc_min_max_temperature(help_sort)
    median_temp=cal_median_temperature(help_sort)
    print("In acending order ",help_sort)
    print("The average is ", average_temps)
    print("The minimum and maximum  value is ", min_max )
    print()


def display_main_menu():
    print("display main menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
def get_user_input():
    user_input=input()
    all_temps = [float(num) for num in (user_input.split(","))]
    return all_temps
    
    

def calc_average_temperature(all_temps):
    length=len(all_temps)
    average= sum(all_temps)/length
    return float(average)



def calc_min_max_temperature(help_sort):

    min_temp=help_sort[0]
    max_temp=help_sort[-1]
    min_max=[min_temp,max_temp]
    min_max = [int(num) for num in min_max]
    return min_max
def sorted_temps(all_temps):
    accending= sorted(all_temps)
    return accending
def cal_median_temperature(help_sort):
    length=len(help_sort)
    middle_index=length//2

    if length%2==0 :
        middle_index=(help_sort[middle_index-1] + help_sort[middle_index])/2
    else:
        middle_index=help_sort[middle_index]
    

if __name__ == "__main__":
    main()
