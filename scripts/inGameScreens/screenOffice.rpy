screen screenOffice:

    tag office

    add officeBackground
    
    imagebutton auto "gui/officeDesktop/officePC_%s.webp":
        xpos 1482
        ypos 593
        action Hide("statusBar"), Show("screenPCOffice")


screen statusBar:
    
    zorder 10

    frame:
        xfill True
        yminimum 180
        ymaximum 180
        
        hbox: #=== MONEY HBOX ===#
            yalign 0.5
            spacing -15
            xalign 0.99
            
            add "gui/statusBar/moneyIcon96.png"
            text "[mcMoney]" yanchor -0.1

        vbox:
            xalign 0.01
            yalign 0.5

            if calendarWeekDay == 1:
                text "SUNDAY"
            elif calendarWeekDay == 2:
                text "MONDAY"
            elif calendarWeekDay == 3:
                text "TUESDAY"
            elif calendarWeekDay == 4:
                text "WEDNESDAY"
            elif calendarWeekDay == 5:
                text "THRUSDAY"
            elif calendarWeekDay == 6:
                text "FRIDAY"
            elif calendarWeekDay == 7:
                text "SATURDAY"

            text "{size=35}[calendarDay]/[calendarMonth]/[calendarYear]{/size}"
        
        imagebutton auto "gui/statusBar/timeIcon_%s.png" action Function(Calendar.nextDay):
            xpos 450


screen screenPCOffice:

    tag office

    zorder 1
    #add wallpaper

    vbox:
        yalign 0.5
        xalign 0.5
    
        textbutton "Start First interview" action Jump("firstMeetClara")
        textbutton "Desligar PC" action Show("statusBar"), Show("screenOffice")



screen screenBillsOffice:
    modal True
    zorder 10    

    frame:
        #style "billsReport"
        xalign 0.5
        yalign 0.5

        vbox:
            text "BILLS REPORT" xalign 0.5
            text "MONEY = [mcMoney]" xalign 0.5
            text "BILL = [moneyDeduct]" xalign 0.5
            text "BILL LEFTING PAY = [mcLoanBill]" xalign 0.5
            #text "NEXT BILL = [((mcLoanBill/10000)*billInterable)]"
            textbutton "OK" action Hide("screenBillsOffice") xalign 0.5


label returnOffice:
    call screen screenOffice        