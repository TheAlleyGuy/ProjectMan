init -1 python:

    class Calendar:

        def nextDay():

            # IMPORTING GLOBAL VARIABLES
            global calendarDay
            global calendarMonth
            global calendarYear
            global calendarWeekDay

            global end30Months
            global end31Months
            
            # INCREASING THE DAY
            calendarDay += 1

            # IF THE MONTH IS FEBRUARY AND THE DAY IS OVER THAN 28 THEN DAY BECOME 01 AND MONTH BECOME MARCH
            if calendarDay > 28 and calendarMonth == 2:
                calendarDay = 1
                calendarMonth = 3
            
            # IF THE DAY IS OVER THAN 30 AND THE MONTH IS IN THE LIST OF MONTH THAT END IN 30 DAYS, THE MONTH IS INCREASED
            elif calendarDay > 30 and calendarMonth in end30Months:
                calendarDay = 1
                calendarMonth += 1

            # IF THE DAY IS OVER THAN 31 AND THE MONTH IS IN THE LIST OF MONTH THAT END IN 31 DAYS, THE MONTH IS INCREASED
            elif calendarDay> 31 and calendarMonth in end31Months:
                calendarDay = 1
                calendarMonth += 1

            # IF THE MONTH IS OVER THAN 12, THAN IS HAPPY NEW YEAR
            if calendarMonth > 12:
                calendarDay = 1
                calendarMonth = 1
                calendarYear += 1


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