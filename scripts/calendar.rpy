init -1 python:

    class Calendar:

        def nextDay():
            global calendarDay
            global calendarMonth
            global calendarYear
            global calendarWeekDay

            global end30Months
            global end31Months
            
            calendarDay += 1

            if calendarDay > 28 and calendarMonth == 2:
                calendarDay = 1
                calendarMonth = 3
            
            elif calendarDay > 30 and calendarMonth in end30Months:
                calendarDay = 1
                calendarMonth += 1

            elif calendarDay> 31 and calendarMonth in end31Months:
                calendarDay = 1
                calendarMonth += 1


            calendarWeekDay += 1

            if calendarWeekDay > 7:
                calendarWeekDay = 1
                
            calendarWeekDayString = "THRUSDAY"
            
            
        def dayOfWeek():

            global calendarWeekDay

            if calendarWeekDay == 1:
                return "SUNDAY"
            elif calendarWeekDay == 2:
                return "MONDAY"
            elif calendarWeekDay == 3:
                return "TUESDAY"
            elif calendarWeekDay == 4:
                return "WEDNESDAY"
            elif calendarWeekDay == 5:
                return "THRUSDAY"
            elif calendarWeekDay == 6:
                return "FRIDAY"
            elif calendarWeekDay == 7:
                return "SATURDAY"