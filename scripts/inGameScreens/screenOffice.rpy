screen screenOffice:

    tag office

    add officeBackground
    
    imagebutton auto "gui/officeDesktop/officePC_%s.webp":
        xpos 1482
        ypos 593
        action Show("screenPCOffice")


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
            text "100" yanchor -0.1

        vbox:
            xalign 0.01
            yalign 0.5

            text "[calendarWeekDayString]"
            text "{size=35}[calendarDay]/[calendarMonth]/[calendarYear]{/size}"
        
        imagebutton auto "gui/statusBar/timeIcon_%s.png" action Function(Calendar.nextDay):
            xpos 400



screen screenPCOffice:

    tag office

    zorder 1
    #add wallpaper
    vbox:
        yalign 0.5
        xalign 0.5
    
        #textbutton "Next Day" action Function(Calendar.nextDay())
        textbutton "Desligar PC" action Show("screenOffice")
    