from datetime import datetime
class Validator:
    
    def verificare_an_bisect(an):
        return (an % 4 == 0 and an % 100 != 0) or (an % 400 == 0)

    def verificare_luna(luna):
        return 1 <= luna <= 12

    def verificare_an(an):
        return an >= 1

    def verificare_zi30(zi, luna):
        return 1 <= zi <= 30 and luna in [4, 6, 9, 11]

    def verificare_zi31(zi, luna):
        return 1 <= zi <= 31 and luna != 2

    def verificare_zi29(zi, luna):
        return luna == 2 and 1 <= zi <= 29
    
    def validare_zi(ziua_sir):
        try:
            ziua_date = datetime.strptime(ziua_sir, "%d.%m.%Y")

            zi = ziua_date.day
            luna = ziua_date.month
            an = ziua_date.year

            if Validator.verificare_an(an):
                if Validator.verificare_luna(luna):
                    if (Validator.verificare_zi30(zi, luna) or Validator.verificare_zi31(zi, luna) or
                            (Validator.verificare_zi29(zi, luna) and Validator.verificare_an_bisect(an))):
                        return True
                    else:
                        raise ValueError("Ziua, luna sau anul datei introduse nu sunt corecte.")
                else:
                    raise ValueError("Luna nu este in intervalul [1,12].")
            else:
                raise ValueError("Anul nu este mai mare ca 1")
        except ValueError as ex:
            raise ex

    def validare_CNP(cnp):
        try:
            if len(cnp) != 13:
                raise ValueError("CNP-ul trebuie să aibă 13 caractere.")

            if not cnp.isdigit():
                raise ValueError("CNP-ul trebuie să conțină doar cifre.")

            sex = int(cnp[0])
            an = int(cnp[1:3])
            luna = int(cnp[3:5])
            ziua = int(cnp[5:7])

            if sex not in [1, 2, 5, 6]:
                raise ValueError("CNP-ul trebuie să înceapă cu 1, 2, 5 sau 6 pentru sex masculin sau feminin.")

            if an < 1 or an > 99:
                raise ValueError("Anul din CNP trebuie să fie între 1 și 99.")

            if luna < 1 or luna > 12:
                raise ValueError("Luna din CNP trebuie să fie între 1 și 12.")

            if ziua < 1 or ziua > 31:
                raise ValueError("Ziua din CNP trebuie să fie între 1 și 31.")

            if luna in [4, 6, 9, 11] and ziua > 30:
                raise ValueError("Ziua din CNP este invalidă pentru luna curentă.")
            elif luna == 2:
                if (an % 4 == 0 and an % 100 != 0) or (an % 400 == 0):
                    if ziua > 29:
                        raise ValueError("Ziua din CNP este invalidă pentru luna curentă într-un an bisect.")
                elif ziua > 28:
                    raise ValueError("Ziua din CNP este invalidă pentru luna curentă.")

            return True
        except ValueError as ex:
            raise ex
        
    def validare_id(id):
        try:
            if not id.isdigit():
                raise ValueError("ID-ul trebuie să conțină doar cifre.")
            return True
        except ValueError as ex:
            raise ex

    def validare_status(status):
        try:
            status_acceptat = ["Returnat", "Nereturnat", "Restant"]
            if status not in status_acceptat:
                raise ValueError("Statusul trebuie să fie 'Returnat', 'Nereturnat' sau 'Restant'.")
            return True
        except ValueError as ex:
            raise ex

    def validare_nume(nume):
        try:
            if not nume.isalpha() and ' ' not in nume:
                raise ValueError("Numele poate conține doar litere și spații.")
            min_length = 3
            if len(nume) < min_length:
                raise ValueError("Numele trebuie să aibă cel puțin {} caractere.".format(min_length))
            max_length = 30
            if len(nume) > max_length:
                raise ValueError("Numele nu poate avea mai mult de {} caractere.".format(max_length))
            return True
        except ValueError as e:
            raise e

    def validare_descriere(descriere):
        try:
            min_length = 3
            if len(descriere) < min_length:
                raise ValueError("Descrierea trebuie să aibă cel puțin {} caractere.".format(min_length))
            return True
        except ValueError as e:
            raise e

    def validare_data(data):
        try:
            Validator.validare_zi(data)
            return True
        except ValueError as ex:
            raise ex

def test_validare_CNP():
        assert Validator.validare_CNP("1930101234567") == True
        assert Validator.validare_CNP("2960202345678") == True

        try:
            Validator.validare_CNP("123")
        except ValueError:
            pass
        else:
            raise AssertionError("Nu a fost aruncată excepția ValueError")

        try:
            Validator.validare_CNP("abcdefghijk1")
        except ValueError:
            pass
        else:
            raise AssertionError("Nu a fost aruncată excepția ValueError")

        try:
            Validator.validare_CNP("1002303456789")
        except ValueError:
            pass
        else:
            raise AssertionError("Nu a fost aruncată excepția ValueError")

def test_validare_id():
        assert Validator.validare_id("123456") == True
        assert Validator.validare_id("987654") == True

        try:
            Validator.validare_id("abc")
        except ValueError:
            pass
        else:
            raise AssertionError("Nu a fost aruncată excepția ValueError")

        try:
            Validator.validare_id("123 456")
        except ValueError:
            pass
        else:
            raise AssertionError("Nu a fost aruncată excepția ValueError")

def test_validare_status():
        assert Validator.validare_status("Returnat") == True
        assert Validator.validare_status("Nereturnat") == True
        assert Validator.validare_status("Restant") == True

        try:
            Validator.validare_status("Inexistent")
        except ValueError:
            pass
        else:
            raise AssertionError("Nu a fost aruncată excepția ValueError")


test_validare_CNP()
test_validare_id()
test_validare_status()
