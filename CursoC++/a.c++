#include "anexos.h"
#include "passvalues.h"

//Parte de Nestor, las funciones 

const std::string currentDateTime()
{
    time_t     now = time(0);
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&now);
    strftime(buf, sizeof(buf), "%Y-%m-%d.%X", &tstruct);

    return buf;
}

int monthDayLength(int month)
{
switch (month)
{
case 1:
    return 31;
    break;
case 2:
   return 28;
    break;
case 3:
    return 31;
    break;
case 4:
    return 30;
    break;
case 5:
    return 31;
    break;
case 6:
    return 30;
    break;
case 7:
  return 31;
    break;
case 8:
    return 31;
    break;
case 9:
    return 30;
    break;
case 10:
   return 31;
    break;
case 11:
   return 30;
    break;
case 12:
    return 31;
    break;
default:
    return 0;
    break;
}
}

int subscriptionRenewal(int currentDay, int month,int daySignedUp = 1)
{
int daysLeft{};

if (currentDay == daySignedUp)
{
    return 1;
}

for (int i{currentDay};; i++)
{

    daysLeft++;

    if (i >= month)
    {
        i = 1;
    }

    if (i == daySignedUp)
    {
        break;
    }

}

return abs(daysLeft);

}

int getDay()
{

std::string raw{currentDateTime()};
std::string dayString{raw.substr(8,2)};
std::stringstream temp{};
int day{};
temp << dayString;
temp >> day;

return day;
}

int getMonth()
{

std::string raw{currentDateTime()};
std::string monthString{raw.substr(5,2)};
std::stringstream temp{};
int month{};
temp << monthString;
temp >> month;
return month;

}


void displayMenu()
{
setlocale(LC_ALL, "spanish");
std::cout << "|===========================================================================|" << '\n';
std::cout << "|         Bienvenido al sistema de subscripcion de documentos               |" << '\n';
std::cout << "|                           DOCU-RED                                        |" << '\n';
std::cout << "|                                                                           |" << '\n';
std::cout << "|     1. Crear un nuevo usuario                                             |" << '\n';
std::cout << "|     2. Iniciar sesion                                                     |" << '\n';
std::cout << "|     3. Revisar estado de cuenta                                           |" << '\n';
std::cout << "|     4. Salir                                                              |" << '\n';
std::cout << "|     a. Revisar lista de usuarios suscritos(DEV)                           |" << '\n';
std::cout << "|                                                                           |" << '\n';
std::cout << "|===========================================================================|" << '\n';
}

void confirmationMenu(std::string nombre, std::string apellido, std::string email, std::string creditCard,std::string date, std:: string CVV, std::string password)
{
std::cout << "|===========================================================================|" << '\n';
std::cout << "|         Estas credenciales son correctas?                                 " << '\n';
std::cout << "|                                                                           " << '\n';
std::cout << "|                                                                           " << '\n';
std::cout << "|     Nombre y apellido:  "<<nombre << " " <<apellido<< "                   " << '\n';
std::cout << "|     Correo electronico: "<<email<< "                                      " << '\n';
std::cout << "|     Tarjeta de Credito: "<<creditCard<< "                                 " << '\n';
std::cout << "|     Fecha vigente:      "<<date << "                                      " << '\n';
std::cout << "|     CVV:                "<<CVV<< "                                        " << '\n';
std::cout << "|     Clave de acceso:    "<<password << "                                  " << '\n';
std::cout << "|                                                                           " << '\n';
std::cout << "|===========================================================================|" << '\n';
}

void textLibrary()
{
std::cout << '\n';
std::cout << '\n';
std::cout << "|===========================================================================|" << '\n';
std::cout << "|                         Cual texto desea leer?                            |" << '\n';
std::cout << "|                                                                           |" << '\n';
std::cout << "|                                                                           |" << '\n';
std::cout << "|     1. Introduction to C/C++                                              |" << '\n';
std::cout << "|     2. Introduction to C++ development                                    |" << '\n';
std::cout << "|     3. Introduction to the compiler, linker, and libraries                |" << '\n';
std::cout << "|     4. Salir                                                              |" << '\n';
std::cout << "|                                                                           |" << '\n';
std::cout << "|     	                                                                    |" << '\n';
std::cout << "|                                                                           |" << '\n';
std::cout << "|===========================================================================|" << '\n';
}

bool doesItHaveSpecialCharacters(std::string &nom)
{
	
for(int i{0}; i < nom.length() ;i++)
{
	if (std::isalpha(nom[i]) == false)
	{
	return true;
	}
}
return false;

}

bool logIn(std::string log, std::string user)
{
	
	if(log == user)
	return true;
		
return false;
}

bool isItAnewUser(std::string old, std::string nuevo)
{
if (old == nuevo)
	{
	return false;
	}
return true;
}

bool isItAnEmail(std::string &email)
{
	for(int i{0}; i < email.length() ;i++)
{
	if (email[i] == '@')
	{
	return true;
	}
}
return false;

}

bool isItACreditCard(std::string &card)
{
	switch (card.length())
	{
		case 13:
		case 14:
		case 15:
		case 16:
		case 17:
		case 18:
		case 19:
		break;
		default: 
		return false;
	}


		for(int i{0}; i < card.length() ;i++)
	{
		if (std::isdigit(card[i]) == false)
		{
		return false;
		}
	}

return true;
}

bool creditCardExpiryLength(std::string card)
{
std::stringstream temp{};
int compare{};
temp << card;
temp >> compare;

//std::cout << card.length() << " " << compare << '\n';

if (card.length() == 4 && compare > 2021)
return true;

return false;
}

bool creditCardExpiryLengthM(std::string card)
{
std::stringstream temp{};
int compare{};
temp << card;
temp >> compare;


if (card.length() == 2 && compare <= 12)
return true;


return false;
}

bool isItcreditCardCVV(std::string card)
{

if (card.length() == 3 || card.length()== 4)
{
  return true;
}

return false;

}

std::string dateTransformation(std::string &expiryM, std::string &expiryY)
{
	std::string dateFormat{expiryM + '/'+ expiryY.substr(2,2)};
	return dateFormat;
}

std::string inputString()
{	
	std::string retval{};
	std::getline(std::cin >> std::ws, retval);
	return retval;
}

int main()
{
bool exit{false};
do
{
displayMenu();
std::cout << ' ' << '\n';
std::cout << "Presione el boton correspondiente a su opcion deseada: ";
char select{static_cast<char>(getch())};
std::cout << '\n';
switch(select)
{
case'1':
{ 
do
{
failure: //Parte de Belen Case '1'
std::cout << "Inserte su primer nombre, sin tildes: " << '\n';
  passValues::nombre = inputString();

std::cout << "Inserte su primer apellido, sin tildes: "<< '\n';
  passValues::apellido = inputString();

passValues::usuarioFinal = passValues::nombre.substr(0,1) + passValues::apellido;
	std::transform(passValues::usuarioFinal.begin(), passValues::usuarioFinal.end(), passValues::usuarioFinal.begin(), ::toupper);

passValues::hasNoSpecialCharacters = !(doesItHaveSpecialCharacters(passValues::usuarioFinal));

std::cout << "Ingrese su correo electronico: "<< '\n';
  passValues::email = inputString();
 
passValues::validEmail = isItAnEmail(passValues::email);
    
std::cout << "Ingrese los numeros frontales de su tarjeta de credito: "<< '\n';
   passValues::ccard = inputString();

passValues::validCreditCard = isItACreditCard(passValues::ccard);
   
std::cout << "Ingrese la epoca en que se expira la tarjeta, sin espacios "<< '\n';
  passValues::expireY = inputString();

passValues::validExpireY = creditCardExpiryLength(passValues::expireY);

std::cout << "Ingrese el mes en que se expira la tarjeta, sin espacios "<< '\n';
  passValues::expireM = inputString();

passValues::validExpireM = creditCardExpiryLengthM(passValues::expireM);

passValues::finalDate = dateTransformation(passValues::expireM, passValues::expireY);

std::cout << "Ingrese los digitos en la parte posterior" << '\n';
  passValues::digits = inputString();

bool validCVV{isItcreditCardCVV(passValues::digits)};

//std::cout << validCVV;

std::cout << "Cree una clave de acceso: "<< '\n'; //crear restricciones??
  passValues::pass = inputString();

if (isItAnewUser(logInInfo::accountEmail, passValues::email) == false || isItAnewUser(logInInfo::accountPassword ,passValues::pass) == false)
{
	std::cout << "\n";
	std::cout << "=============================================================\n";
	std::cout << "Ya se ha creado una cuenta con esas credenciales, porfavor intente de nuevo.\n";
	std::cout << "=============================================================\n";
	std::cout << '\n';
	goto failure;

}


if(passValues::hasNoSpecialCharacters == false || passValues::validEmail == false || passValues::validCreditCard == false || passValues::validExpireY == false ||passValues::validExpireM == false || validCVV == false)
{
//std::cout << std::boolalpha << "specialC: " << passValues::hasNoSpecialCharacters << " validEmail: " << passValues::validEmail << " CreditCard: " <<passValues::validCreditCard << " Year:" << passValues::validExpireY << " Month " << passValues::validExpireM << " CVV: " <<  validCVV << '\n';
std::cout << "Uno o mas parametros han sido ingresados erroneamente, porfavor intente de nuevo" << '\n';
std::cin.ignore(10000000000, '\n');
goto failure;
}

confirmationMenu(passValues::nombre, passValues::apellido, passValues::email, passValues::ccard, passValues::finalDate ,passValues::digits, passValues::pass);
std::cout << ' ' << '\n';
std::cout << " (s/n)? " << '\n';
char end{static_cast<char>(getch())};
if(end == 's')
{
std::cout << "\n";
std::cout << "=============================================================\n";
std::cout << "Usuario agregado exitosamente!" << '\n';
std::cout << "=============================================================\n";
break;
}
}while(true);
break;
}
case '2':
{
int logInAttempts{0};
while (logInAttempts <= 3)
{
std::cout << "Ingrese su correo electronico" << '\n';
std::string logInEmail{inputString()};
std::cout << "Ingrese su clave de acceso" << '\n';
std::string logInPassword{inputString()};
if (logIn(logInEmail,logInInfo::accountEmail)&&logIn(logInPassword ,logInInfo::accountPassword))
{
	std::cout << "\n";
	std::cout << "=============================================================\n";
	std::cout << "Sesion iniciada exitosamente!\n";
	std::cout << "=============================================================\n";
	std::cout << '\n';
	break;
}

std::cout << "\n";
	std::cout << "==================================================================================\n";
	std::cout << "Ingreso alguna de las credenciales incorrectamente, porfavor intente de nuevo\n";
	std::cout << "================================================================================\n";
	std::cout << '\n';

logInAttempts += 1;
}
if (logInAttempts > 3)
{
std::cout << "\n";
std::cout << "=============================================================================\n";
std::cout << "Se han realizado demasiados intentos de inicio de sesion, intente mas tarde\n";
std::cout << "=============================================================================\n";
std::cout<< '\n';
break;
}
bool exit2{false};
while(exit2 == false)
{
textLibrary();
std::cout << ' ' << '\n';
std::cout << "Presione el boton correspondiente a su opcion deseada: ";
char select2{static_cast<char>(getch())};
std::cout << '\n';
switch (select2)
{
case '1':
{
	   std::ifstream f("IntroductionCPP.txt");

    if (f.is_open())
        std::cout << f.rdbuf();
std::cout << '\n';
system("pause");

break;
}
case '2': 
{
	   std::ifstream f("IntroductionToCPPDevelopment.txt");

    if (f.is_open())
        std::cout << f.rdbuf();
std::cout << '\n';
system("pause");
break;
}
case '3':
{
	   std::ifstream f("IntroductionToTheCompiler.txt");

    if (f.is_open())
        std::cout << f.rdbuf();
std::cout << '\n';
system("pause");
break;
}
case '4':
{
	exit2 = true;
break;
}
default:
std::cout << "\n";
std::cout << "=============================================================\n";
std::cout << "No existe esa opcion\n";
std::cout << "=============================================================\n";
std::cout << '\n';
}
}
}
break;
case'3':
{
int hoy{getDay()};
int mes{monthDayLength(getMonth())};
std::cout << "\n";
std::cout << "===================================================================================\n";
std::cout << "Faltan " << subscriptionRenewal(hoy,mes) << " dias para renovar su subscripcion\n";
std::cout << "===================================================================================\n";
std::cout<< '\n';
break;
}
case'4':
{
exit = true;
break;
}
default:
std::cout << "\n";
std::cout << "=============================================================\n";
std::cout << "No existe esa opcion\n";
std::cout << "=============================================================\n";
std::cout << '\n';
};
}while(exit == false);
return 0;
}


