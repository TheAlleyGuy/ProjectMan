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
        background Frame("gui/input_frame_bg.png", Borders(25,25,25,25))
        xfill True
        xpadding 50
        xmargin 10
        yminimum 180
        ymaximum 180
        ypos 15


        
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
    add "gui/officeDesktop/desktop_office_wallpaper.jpg"


    frame: ### ICONS
        align (0.5, 0.0)
        background "#ecd6d600"
        ymaximum 1950
        
        vpgrid: 

            cols 3

            draggable True
            mousewheel True
            
            xfill True
            yfill True

            scrollbars "vertical"

            # Since we have scrollbars, we have to position the side, rather
            # than the vpgrid proper.
            side_xalign 0.5

            for i in range(1, 50):

                imagebutton auto "gui/officeDesktop/desktopMailIcon_%s.webp":
                    action Jump("firstMeetClara") 
                    at office_desktop_icon

    frame: ### TASKBAR

        background "#00000000"
        xalign 0.0
        yalign 1.0
        
        xfill True

        hbox:
            imagebutton auto "gui/officeDesktop/office_desktop_turnoff_%s.webp":
                action Show("statusBar"), Show("screenOffice") 
                at office_desktop_icon 




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