BEGIN
    DISPLAY "Secure Password Generator"
    REPEAT
        DISPLAY "Enter password length (4-128):"
        INPUT length
        DISPLAY "Include lowercase letters? (Yes/No)"
        INPUT lowercase
        DISPLAY "Include uppercase letters? (Yes/No)"
        INPUT uppercase
        DISPLAY "Include numbers? (Yes/No)"
        INPUT numbers
        DISPLAY "Include symbols? (Yes/No)"
        INPUT symbols

        IF length < 4 OR length > 128 THEN
            DISPLAY "Invalid password length"
        ELSE
            characters = ""

            IF lowercase = Yes THEN
                ADD "abcdefghijklmnopqrstuvwxyz" TO characters
            ENDIF
            IF uppercase = Yes THEN
                ADD "ABCDEFGHIJKLMNOPQRSTUVWXYZ" TO characters
            ENDIF
            IF numbers = Yes THEN
                ADD "0123456789" TO characters
            ENDIF
            IF symbols = Yes THEN
                ADD "!@#$%&*" TO characters
            ENDIF

            IF characters = "" THEN
                DISPLAY "Please select at least one option"
            ELSE
                password = ""
                FOR i = 1 TO length
                    SELECT a secure random character FROM characters
                    ADD character TO password
                ENDFOR
                DISPLAY "Your password is:", password
            ENDIF
        ENDIF

        DISPLAY "Generate another password? (Yes/No)"
        INPUT again
    UNTIL again = No
END