#include <cstdlib>
#include <iostream>
#include <fstream>
#include <windows.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <clocale>
#include <ctype.h>
#include <conio.h>
#include <string>
#include <ctime>

using namespace std;

// fecha
string fecha;


int len = 0;
int salida = 1;
int medidor;

string nombre, apellido, nacimiento, correo, tempcorreo, PassUsu, tempPassUsu;
string cedula, tempCedula, tempCedula2;

char opca;

bool encontrado = false;
bool minimo = false;
bool mayus = false;
bool minuscula = false;
bool especial = false;
bool seguir = true;
bool valida = false;


string Admin = "Admin";
string Password = "123";

//-----------------------------------------------
// Seccion de montos y acciones

float cdinero; //la cantidad que se mueve
float ctotal; // la cantidad de dinero total de una cuenta
float temptotal;
float checker;

string maccion; // puede ser transferencia / deposito / retiro

bool ValidAccion = false;

//-----------------------------------------------

void MenuPrincipal();
void MenuAccionesD();
void MenuDependiente();

string obtenerfecha(){
    time_t t = time(nullptr);
    tm* now = localtime(&t);
 
    char buffer[128];
    strftime(buffer, sizeof(buffer), "%m-%d-%Y", now);
    return buffer;
}


void ContraValida()
{
	
	string contra;
	
	bool pass=false;
	while(!pass){
	cout << "\n\tIngrese una contraseña con un minimo 8 digitos y maximo 20\n";
	cout << "\tIncluya por lo menos un caracter en minuscula, mayuscula y especial o un numero\n";
	cout << "\t** No use espacios **\n\n";
	cout << "\tContraseña ->  ";

	char caracter;
	caracter = getch();
	contra="";
	
	while (caracter !=13) { //Lee la contrasenia hasta que se precione el ASCII 13 (ENTER)
	
		if (caracter != 8){	//Condicion para evitar que tome el ASCII 8 (BACKSPACE) como un caracter mas
			contra.push_back(caracter);
			cout<<"*"; //Imprime asteriscos para que no se vea la contrasenha 
		} else {
			if (contra.length()>0){
				cout<< "\b \b"; //Imprime espacios en blanco para poder borrar con BACKSPACE
				contra=contra.substr(0, contra.length()-1);
				}
			}	
	caracter = getch();
		}
		
	medidor=contra.length();	//	"medidor" lee la cantidad de caracteres de la contraseña
	
	if (medidor >= 8)	// "medidor" se compara la contraseña hasta que sea >=8
	{minimo = true; }
	
	for (int i = 0;i < medidor;i++){	//Ciclo que lee la contraseña para ver que tenga al menos una mayuscula
		if(isupper(contra[i])){
			mayus = true;
		}
	}
	
	for (int i = 0;i < medidor;i++){	//Ciclo que lee la contraseña para ver que tenga al menos una minuscula
		if(islower(contra[i])){
			minuscula = true;
		}
	}
	
	for (int i = 0;i < medidor;i++){	//Ciclo que lee la contraseña para ver que tenga al menos un caracter especial o un numero
		if(isalpha(contra[i])==false){
			especial = true;
		}
	}
	if(minimo && mayus && minuscula && especial){
		cout<<"\n\n\tLa contraseña cumple con los requisitos"<<endl;
		pass=true;
	} else {
		cout<<"\n\n\tLa contraseña no cumple con los requisitos."<<endl; //si no cumple los requisitos la contraseña se vuelve a intentar
	}
}
	PassUsu = contra;
}

void AgregarN()
{
	///Variables de la biblioteca fstream para el manejo de archivos
	ofstream escritura;
	ifstream consulta;

	do{
	escritura.open("UsuariosN.txt", ios::out | ios::app);//crea y escribe, si ya tiene texto une al final del archivo
	consulta.open("UsuariosN.txt", ios::in);//solamente consulta o lee usando la variable sobre el archivo físico 

	if (escritura.is_open() && consulta.is_open()){


        	bool repetido=false;

        	cout<<"\n";
        	cout<<"\tIngresa la cedula del usuario:	";
        	cin>>tempCedula;
             	 
        	///A continuación se aplica el tipo de lectura de archivos secuencial
        	consulta>>cedula;
        	while (!consulta.eof()){
            	consulta>>nombre>>apellido>>nacimiento>>correo>>PassUsu>>ctotal;
            	if (tempCedula==cedula){
                	cout<<"\t\tYa existe un usuario con esa cedula...\n";
                	repetido=true;
                	break;
            	}
            	consulta>>cedula;
        	}

        	if (repetido==false){
            	cout<<"\tIngresa el primer nombre del usuario: ";
            	cin>>nombre;
            	
            	cout<<"\tIngresa el primer apellido del usuario: ";
            	cin>>apellido;
            	
            	
            	cout<<"\tIngresa la fecha de nacimiento (dd/mm/aa): ";
            	cin>>nacimiento;
            	
            	cout<<"\tIngresa el correo del usuario: ";
            	cin>>correo;
            	
            	ContraValida();
				
				ctotal = 0;
				
            	//ESCRIBIENDO LOS DATOS CAPTURADOS POR EL USUARIO EN EL ARCHIVO
            	escritura<<tempCedula<<" "<<nombre<<" "<<apellido<<" "<<nacimiento<<" "<<correo<<" "<<PassUsu<<" "<<ctotal<<endl;
            	cout<<"\n\tUsuario agregado...\n";
        	}

        	cout<<"\n\tDeseas ingresar otro usuario? (S/N): ";
        	cin>>opca;

	}else{
    	cout<<"El archivo no se pudo abrir \n";
	}

	escritura.close();
	consulta.close();

	}while (opca=='S' or opca=='s');

}

void AgregarD()
{
	///Variables de la biblioteca fstream para el manejo de archivos
	ofstream escritura;
	ifstream consulta;

	do{
	escritura.open("UsuariosD.txt", ios::out | ios::app);//crea y escribe, si ya tiene texto une al final del archivo
	consulta.open("UsuariosD.txt", ios::in);//solamente consulta o lee usando la variable sobre el archivo físico UsuariosN.txt

	if (escritura.is_open() && consulta.is_open()){


        	bool repetido=false;

        	cout<<"\n";
        	cout<<"\tIngresa la cedula del dependiente:	";
        	cin>>tempCedula;

       	 
        	///A continuación se aplica el tipo de lectura de archivos secuencial
        	consulta>>cedula;
        	while (!consulta.eof()){
            	consulta>>nombre>>apellido>>nacimiento>>correo>>PassUsu;
            	if (tempCedula==cedula){
                	cout<<"\t\tYa existe un dependiente con esa cedula...\n";
                	repetido=true;
                	break;
            	}
            	consulta>>cedula;
        	}

        	if (repetido==false){
            	cout<<"\tIngresa el primer nombre del dependiente: ";
            	cin>>nombre;
            	
            	cout<<"\tIngresa el primer apellido del usuario: ";
            	cin>>apellido;
            	
            	cout<<"\tIngresa la fecha de nacimiento (dd/mm/aa): ";
            	cin>>nacimiento;
            	
            	cout<<"\tIngresa el correo del dependiente:	";
            	cin>>correo;
            
            	ContraValida();
            		
            	//ESCRIBIENDO LOS DATOS CAPTURADOS POR EL USUARIO EN EL ARCHIVO
            	escritura<<tempCedula<<" "<<nombre<<" "<<apellido<<" "<<nacimiento<<" "<<correo<<" "<<PassUsu<<endl;
            	cout<<"\n\tDependiente agregado...\n";
        	}

        	cout<<"\n\tDeseas ingresar otro depenidente? (S/N): ";
        	cin>>opca;

	}else{
    	cout<<"El archivo no se pudo abrir \n";
	}

	escritura.close();
	consulta.close();

	}while (opca=='S' or opca=='s');

}

void EliminarN()
{
	ofstream aux;
	ifstream lectura;

	encontrado=false;

	aux.open("tempUsuario.txt", ios::out);
	lectura.open("UsuariosN.txt", ios::in);

	if (aux.is_open() && lectura.is_open()){

    	cout<<"\n";
    	cout<<"\tIngresa la cedula del usuario que deseas eliminar: ";
    	cin>>tempCedula;
       	 
        	///De nuevo se aplica el tipo de lectura de archivos secuencial, esto quiere decir que lee campo por campo hasta
        	///hasta llegar al final del archivo gracias a la función .eof()
        	lectura>>cedula;
        	while (!lectura.eof()){
            	lectura>>nombre>>apellido>>nacimiento>>correo>>PassUsu;
            	if (tempCedula==cedula){
                    	encontrado=true;
                    	cout<<"\n";
                    	cout<<"\tCedula:	"<<cedula<<endl;
                    	cout<<"\tNombre:   "<<nombre<<" "<<apellido<<endl;
                    	cout<<"\tFecha Nacimiento: "<<nacimiento<<endl;
                    	cout<<"\tCorreo:	"<<correo<<endl;
                    	cout<<"\t________________________________\n\n";
                    	cout<<"\tRealmente deseas eliminar el registro actual (S/N)? ---> ";
                    	cin>>opca;

                    	if (opca=='S' or opca=='s'){
                        	cout<<"\n\n\t\t\tRegistro eliminado...\n\n\t\t\a";
                    	}else{
                        	aux<<cedula<<" "<<nombre<<" "<<apellido<<" "<<nacimiento<<" "<<correo<<" "<<PassUsu<<endl;
                    	}

                	}else{
                    	aux<<cedula<<" "<<nombre<<" "<<apellido<<" "<<nacimiento<<" "<<correo<<" "<<PassUsu<<endl;
                	}
            	lectura>>cedula;
        	}
	}else{
    	cout<<"\n\tEl archivo no se pudo abrir \n";
	}

	if (encontrado==false){
            	cout<<"\n\tNo se encontro ningun usuario con la cedula: "<<tempCedula<<"\n\n\t\t\t";
        	}

	aux.close();
	lectura.close();
	remove ("UsuariosN.txt");
	rename("tempUsuario.txt", "UsuariosN.txt");

}

void EliminarD()
{
	ofstream aux;
	ifstream lectura;

	encontrado=false;

	aux.open("tempUsuario.txt", ios::out);
	lectura.open("UsuariosD.txt", ios::in);

	if (aux.is_open() && lectura.is_open()){

    	cout<<"\n";
    	cout<<"\tIngresa la cedula del usuario que deseas eliminar: ";
    	cin>>tempCedula;
       	 
        	///De nuevo se aplica el tipo de lectura de archivos secuencial, esto quiere decir que lee campo por campo hasta
        	///hasta llegar al final del archivo gracias a la función .eof()
        	lectura>>cedula;
        	while (!lectura.eof()){
            	lectura>>nombre>>apellido>>nacimiento>>correo>>PassUsu;
            	if (tempCedula==cedula){
                    	encontrado=true;
                    	cout<<"\n";
                    	cout<<"\tCedula:	"<<cedula<<endl;
                    	cout<<"\tNombre:   "<<nombre<<" "<<apellido<<endl;
                    	cout<<"\tFecha Nacimiento: "<<nacimiento<<endl;
                    	cout<<"\tCorreo:	"<<correo<<endl;
                    	cout<<"\t________________________________\n\n";
                    	cout<<"\tRealmente deseas eliminar el registro actual (S/N)? ---> ";
                    	cin>>opca;

                    	if (opca=='S' or opca=='s'){
                        	cout<<"\n\n\t\t\tRegistro eliminado...\n\n\t\t\a";
                    	}else{
                        	aux<<cedula<<" "<<nombre<<" "<<apellido<<" "<<nacimiento<<" "<<correo<<" "<<PassUsu<<endl;
                    	}

                	}else{
                    	aux<<cedula<<" "<<nombre<<" "<<apellido<<" "<<nacimiento<<" "<<correo<<" "<<PassUsu<<endl;
                	}
            	lectura>>cedula;
        	}
	}else{
    	cout<<"\n\tEl archivo no se pudo abrir \n";
	}

	if (encontrado==false){
            	cout<<"\n\tNo se encontro ningun dependiente con la cedula: "<<tempCedula<<"\n\n\t\t\t";
        	}

	aux.close();
	lectura.close();
	remove ("UsuariosD.txt");
	rename("tempUsuario.txt", "UsuariosD.txt");

}

void consultasN()
{
	//Lectura de archivos

	ifstream lectura;
	lectura.open("UsuariosN.txt", ios::out | ios::in);//CREA, ESCRIBE O LEE
	if (lectura.is_open()){
   	//LEYENDO Y MOSTRANDO CADA CAMPO DEL ARCHIVO DE FORMA SECUENCIAL
   	lectura>>cedula;
   	while (!lectura.eof()){
        	lectura>>nombre>>apellido>>nacimiento>>correo>>PassUsu>>ctotal;
        	cout<<"\n";
        	cout<<"\tCedula:	"<<cedula<<endl;
        	cout<<"\tNombre:   "<<nombre<<" "<<apellido<<endl;
        	cout<<"\tFecha nacimiento: "<<nacimiento<<endl;
        	cout<<"\tCorreo:	"<<correo<<endl;
        	lectura>>cedula;
        	cout<<"\t________________________________\n";
   	}

	}else{
    	cout<<"El archivo no se pudo abrir \n";
	}
	lectura.close();
}

void consultasD()
{
	//Lectura de archivos

	ifstream lectura;
	lectura.open("UsuariosD.txt", ios::out | ios::in);//CREA, ESCRIBE O LEE
	if (lectura.is_open()){
   	//LEYENDO Y MOSTRANDO CADA CAMPO DEL ARCHIVO DE FORMA SECUENCIAL
   	lectura>>cedula;
   	while (!lectura.eof()){
        	lectura>>nombre>>apellido>>nacimiento>>correo>>PassUsu;
        	cout<<"\n";
        	cout<<"\tCedula:	"<<cedula<<endl;
        	cout<<"\tNombre:   "<<nombre<<" "<<apellido<<endl;
        	cout<<"\tFecha nacimiento: "<<nacimiento<<endl;
        	cout<<"\tCorreo:	"<<correo<<endl;
        	lectura>>cedula;
        	cout<<"\t________________________________\n";
   	}

	}else{
    	cout<<"El archivo no se pudo abrir \n";
	}
	lectura.close();
}

void loginU()
{
	
	ifstream lectura;
	lectura.open("UsuariosN.txt", ios::out | ios::in);
	
	bool a = false;
	encontrado=false;

	if (lectura.is_open()){
    	cout<<"\n\tIngrese la cedula del usuario: ";
    	cin>>tempCedula;

    	lectura>>cedula;
    	while(!lectura.eof()){
        	lectura>>nombre>>apellido>>nacimiento>>correo>>PassUsu>>ctotal;
        	
    	//comparar cada registro para ver si es encontrado
    	
    	if(tempCedula==cedula){
        	encontrado=true;
    		
    		
    		cout<<"\n\tIngrese la contraseña: ";
    			char caracter;
				caracter = getch();
				tempPassUsu="";
			while (caracter !=13) { //Lee la contrasenia hasta que se precione el ASCII 13 (ENTER)
	
			if (caracter != 8){	//Condicion para evitar que tome el ASCII 8 (BACKSPACE) como un caracter mas
			tempPassUsu.push_back(caracter);
			cout<<"*"; //Imprime asteriscos para que no se vea la contrasenha 
			} else {
			if (tempPassUsu.length()>0){
				cout<< "\b \b"; //Imprime espacios en blanco para poder borrar con BACKSPACE
				tempPassUsu=tempPassUsu.substr(0, tempPassUsu.length()-1);
				}
			}	
			caracter = getch();
			}

			
	    	if(tempPassUsu==PassUsu){
	    	
	    		float ctotalt;
	    		ctotalt = ctotal; 
	    	
				ofstream escritura2;
				ifstream consulta2;
				
				
				
				escritura2.open("Movimientos.txt", ios::out | ios::app);//crea y escribe, si ya tiene texto une al final del archivo
				consulta2.open("Movimientos.txt", ios::in);//solamente consulta o lee usando la variable sobre el archivo físico 
				
				if (escritura2.is_open() && consulta2.is_open()){
				    	
				    		
			    	ofstream aux;
					ifstream lectura;
						
					encontrado=false;
					ValidAccion = false;
					
					
					aux.open("tempUsuario.txt", ios::out);
					lectura.open("UsuariosN.txt", ios::in);
						
					if (aux.is_open() && lectura.is_open()){
						
						string tempCedula2;
						
				    	system("cls");
			    		cout<<"\n\tIngrese el usuario al que desea transferir: ";
			    		cin>>tempCedula2;
			    		
						lectura>>cedula;
						
						while (!lectura.eof()){
							
							lectura>>nombre>>apellido>>nacimiento>>correo>>PassUsu>>ctotal;
							
					        if (tempCedula2==cedula){
					            encontrado=true;
					            
					        	cout<<"\n\tIngrese la cantidad de dinero que desea depositar a la cuenta a nombre de "<<nombre<<" "<<apellido<<"\n\t ---> ";
					            cin>>temptotal;
					            
								if (temptotal > 0){
								
		
									checker = ctotalt - temptotal;
					
									if (checker < 0){
							
									system("cls");
									cout<<"\n\n\t** Usted no tiene saldo suficiente para transferir esa cantidad **\n\t\t";
									system("pause");
									system("cls");
									}else {
						
										ctotal = ctotal + temptotal;
										
										cout<<"\n\n **"<<cedula<<"**\n";
										
										aux<<cedula<<" "<<nombre<<" "<<apellido<<" "<<nacimiento<<" "<<correo<<" "<<PassUsu<<" "<<ctotal<<endl;
								
										
										cout<<"\n\n **"<<ctotal<<"**\n";
										
					            		cout<<"\n\n\t\ttransacción realizada con exito...";
					            		ValidAccion = true;
				
									}
									
				        			}
									else{
									system("cls");
									cout<<"\n\n\t** Ha ingresado un valor incorrecto, reinicie el proceso **";
									system("pause");
									system("cls");
									aux<<cedula<<" "<<nombre<<" "<<apellido<<" "<<nacimiento<<" "<<correo<<" "<<PassUsu<<" "<<ctotal<<endl;
									}
							}else{
								aux<<cedula<<" "<<nombre<<" "<<apellido<<" "<<nacimiento<<" "<<correo<<" "<<PassUsu<<" "<<ctotal<<endl;
								}
							
						
							lectura>>cedula;
						}
					
						if (encontrado==false){
			        	cout<<"\n\tNo se encontro ningun usuario con la cedula: "<<tempCedula2<<"\n\n\t\t\t";
			    		}
			    		
						}else{
						cout<<"\n\tEl archivo no se pudo abrir \n";
						}
					
			    		
					aux.close();
					lectura.close();
					remove("UsuariosN.txt");
					rename("tempUsuario.txt", "UsuariosN.txt");
			    		
				
					}else{
			   			cout<<"El archivo no se pudo abrir \n";
						}
						
					escritura2.close();
					consulta2.close();
				
			if (ValidAccion){
			
				ofstream aux;
				ifstream lectura;
									
				aux.open("tempUsuario.txt", ios::out);
				lectura.open("UsuariosN.txt", ios::in);
					
				if (aux.is_open() && lectura.is_open()){
					
					lectura>>cedula;
					while (!lectura.eof()){
						lectura>>nombre>>apellido>>nacimiento>>correo>>PassUsu>>ctotal;
				        if (tempCedula==cedula){
				        	
				        	cout<<"\n\n"<<checker;
							ctotal =checker;
							cout<<"\n\n"<<ctotal;
	
							aux<<cedula<<" "<<nombre<<" "<<apellido<<" "<<nacimiento<<" "<<correo<<" "<<PassUsu<<" "<<ctotal<<endl;
				    		cout<<"\n\n\t\tRetiro realizado con exito...";
				    		
								
							}
						else{
							aux<<cedula<<" "<<nombre<<" "<<apellido<<" "<<nacimiento<<" "<<correo<<" "<<PassUsu<<" "<<ctotal<<endl;
							}
						lectura>>cedula;
					}
				}else{
					cout<<"\n\tEl archivo no se pudo abrir \n";
					}
				
				a = true;
				aux.close();
				lectura.close();
				remove ("UsuariosN.txt");
				rename("tempUsuario.txt", "UsuariosN.txt");	
				}
				
				if (ValidAccion){
			
				ofstream aux;
				ifstream lectura;
									
				aux.open("tempUsuario.txt", ios::out);
				lectura.open("UsuariosN.txt", ios::in);
					
				if (aux.is_open() && lectura.is_open()){
					
					lectura>>cedula;
					while (!lectura.eof()){
						lectura>>nombre>>apellido>>nacimiento>>correo>>PassUsu>>ctotal;
				        if (tempCedula2==cedula){
				        	
				        
							ctotal = ctotal + temptotal;
							cout<<"\n\n"<<ctotal;
	
							aux<<cedula<<" "<<nombre<<" "<<apellido<<" "<<nacimiento<<" "<<correo<<" "<<PassUsu<<" "<<ctotal<<endl;
				    		cout<<"\n\n\t\tRetiro realizado con exito...";
				    		
								
							}
						else{
							aux<<cedula<<" "<<nombre<<" "<<apellido<<" "<<nacimiento<<" "<<correo<<" "<<PassUsu<<" "<<ctotal<<endl;
							}
						lectura>>cedula;
					}
				}else{
					cout<<"\n\tEl archivo no se pudo abrir \n";
					}
				
				a = true;
				aux.close();
				lectura.close();
				remove ("UsuariosN.txt");
				rename("tempUsuario.txt", "UsuariosN.txt");	
				}
					
	        break;
	    	}
	    	else{
	    		cout<<"\n\t\tContraseña incorrecta";
			}
    	
        	break;
    	}//fin del if mostrar encontrado
		
    	//lectura adelantada
    	lectura>>cedula;
    	}//fin del while
    	if (encontrado==false){
        	cout<<"\n\n\tNo hay usuario con la cedula: "<<tempCedula<<"\n\n\t\t\t";
    	}
    	
	}
	else{
    	cout<<"\n\tAun no se pudo abrir el archivo...";
	}
	lectura.close();
	
	/*if (a){
	remove ("UsuariosN.txt");
	rename("tempUsuario.txt", "UsuariosN.txt");	
	}//else {remove ("tempUsuario.txt");}
	*/
}


void loginD()
{
	
	ifstream lectura;
	lectura.open("UsuariosD.txt", ios::out | ios::in);

	encontrado=false;

	if (lectura.is_open()){
    	cout<<"\n\tIngrese la cedula del dependiente: ";
    	cin>>tempCedula;

    	lectura>>cedula;
    	while(!lectura.eof()){
        	lectura>>nombre>>apellido>>nacimiento>>correo>>PassUsu;
        	
    	//comparar cada registro para ver si es encontrado
    	
    	if(tempCedula==cedula){
        	encontrado=true;
    		
    		
    		cout<<"\n\tIngrese la contraseña: ";
    			char caracter;
				caracter = getch();
				tempPassUsu="";
			while (caracter !=13) { //Lee la contrasenia hasta que se precione el ASCII 13 (ENTER)
	
			if (caracter != 8){	//Condicion para evitar que tome el ASCII 8 (BACKSPACE) como un caracter mas
			tempPassUsu.push_back(caracter);
			cout<<"*"; //Imprime asteriscos para que no se vea la contrasenha 
			} else {
			if (tempPassUsu.length()>0){
				cout<< "\b \b"; //Imprime espacios en blanco para poder borrar con BACKSPACE
				tempPassUsu=tempPassUsu.substr(0, tempPassUsu.length()-1);
				}
			}	
			caracter = getch();
			}

	    	if(tempPassUsu==PassUsu){
				
				MenuAccionesD();
	        	break;
	    	}
	    	else{
	    		cout<<"\n\t\tContraseña incorrecta";
			}
    	
        	break;
    	}//fin del if mostrar encontrado

    	//lectura adelantada
    	lectura>>cedula;
    	}//fin del while
    	if (encontrado==false){
        	cout<<"\n\n\tNo hay dependiente con la cedula: "<<tempCedula<<"\n\n\t\t\t";
    	}
	}
	else{
    	cout<<"\n\tAun no se pudo abrir el archivo...";
	}

	lectura.close();
	
}

void buscarN()
{
	ifstream lectura;
	lectura.open("UsuariosN.txt", ios::out | ios::in);

	encontrado=false;

	if (lectura.is_open()){
    	cout<<"\n\tIngresa la cedula del usuario que deseas buscar: ";
    	cin>>tempCedula;

    	lectura>>cedula;
    	while(!lectura.eof()){
        	lectura>>nombre>>apellido>>nacimiento>>correo>>PassUsu>>ctotal;
    	//comparar cada registro para ver si es encontrado

    	if(tempCedula==cedula){
        	cout<<"\n";
        	cout<<"\tCedula:	"<<cedula<<endl;
        	cout<<"\tNombre:   "<<nombre<<" "<<apellido<<endl;
        	cout<<"\tFecha nacimiento: "<<nacimiento<<endl;
        	cout<<"\tCorreo:	"<<correo<<endl;
        	cout<<"\t________________________________\n";
        	encontrado=true;
        	break;
    	}//fin del if mostrar encontrado

    	//lectura adelantada
    	lectura>>cedula;
    	}//fin del while
    	if (encontrado==false){
        	cout<<"\n\n\tNo hay usuario con la cedula: "<<tempCedula<<"\n\n\t\t\t";
    	}
	}else{
    	cout<<"\n\tAun no se pudo abrir el archivo...";
	}

	lectura.close();
}

void buscarD()
{
	ifstream lectura;
	lectura.open("UsuariosD.txt", ios::out | ios::in);

	encontrado=false;

	if (lectura.is_open()){
    	cout<<"\n\tIngresa la cedula del dependiente que deseas buscar: ";
    	cin>>tempCedula;

    	lectura>>cedula;
    	while(!lectura.eof()){
        	lectura>>nombre>>apellido>>nacimiento>>correo>>PassUsu;
    	//comparar cada registro para ver si es encontrado

    	if(tempCedula==cedula){
        	cout<<"\n";
        	cout<<"\tCedula:	"<<cedula<<endl;
        	cout<<"\tNombre:   "<<nombre<<" "<<apellido<<endl;
        	cout<<"\tFecha nacimiento: "<<nacimiento<<endl;
        	cout<<"\tCorreo:	"<<correo<<endl;
        	cout<<"\t________________________________\n";
        	encontrado=true;
        	break;
    	}//fin del if mostrar encontrado

    	//lectura adelantada
    	lectura>>cedula;
    	}//fin del while
    	if (encontrado==false){
        	cout<<"\n\n\tNo hay dependiente con la cedula: "<<tempCedula<<"\n\n\t\t\t";
    	}
	}else{
    	cout<<"\n\tAun no se pudo abrir el archivo...";
	}

	lectura.close();
}

void modificarN()
{
	ofstream aux;
	ifstream lectura;

	encontrado=false;

	aux.open("tempUsuario.txt", ios::out);
	lectura.open("UsuariosN.txt", ios::in);

	if (aux.is_open() && lectura.is_open()){

    	cout<<"\n";
    	cout<<"\tIngresa la cedula del usuario que deseas modificar: ";
    	cin>>tempCedula;

        	lectura>>cedula;
        	while (!lectura.eof()){
            	lectura>>nombre>>apellido>>nacimiento>>correo>>PassUsu>>ctotal;
            	if (tempCedula==cedula){
                	encontrado=true;
                	cout<<"\n";
                	cout<<"\tCedula:	"<<cedula<<endl;
                	cout<<"\tNombre:   "<<nombre<<" "<<apellido<<endl;
                	cout<<"\tFecha nacimiento: "<<nacimiento<<endl;
                	cout<<"\tCorreo:	"<<correo<<endl;
                	cout<<"\t________________________________\n\n";
               	 
                	//sub menu para opciones de las cuales desea modificar y en bucle para no estar entra y sale..8
               	 
                	cout<<"\tIngresa el nuevo correo del usuario con la cedula: "<<tempCedula<<"\n\n\t---> ";
                	cin>>tempcorreo;

                	aux<<cedula<<" "<<nombre<<" "<<apellido<<" "<<nacimiento<<" "<<correo<<" "<<PassUsu<<ctotal<<endl;
                	cout<<"\n\n\t\t\tRegistro modificado...\n\t\t\a";
                	}else{
                	aux<<cedula<<" "<<nombre<<" "<<apellido<<" "<<nacimiento<<" "<<correo<<" "<<PassUsu<<ctotal<<endl;
                	}
            	lectura>>cedula;
        	}
	}else{
    	cout<<"\n\tEl archivo no se pudo abrir \n";
	}

	if (encontrado==false){
            	cout<<"\n\tNo se encontro ningun usuario con la cedula: "<<tempCedula<<"\n\n\t\t\t";
        	}

	aux.close();
	lectura.close();
	remove ("UsuariosN.txt");
	rename("tempUsuario.txt", "UsuariosN.txt");
}

void modificarD()
{
	ofstream aux;
	ifstream lectura;

	encontrado=false;

	aux.open("tempUsuario.txt", ios::out);
	lectura.open("UsuariosD.txt", ios::in);

	if (aux.is_open() && lectura.is_open()){

    	cout<<"\n";
    	cout<<"\tIngresa la cedula del dependiente que deseas modificar: ";
    	cin>>tempCedula;

        	lectura>>cedula;
        	while (!lectura.eof()){
            	lectura>>nombre>>apellido>>nacimiento>>correo>>PassUsu;
            	if (tempCedula==cedula){
                	encontrado=true;
                	cout<<"\n";
                	cout<<"\tCedula:	"<<cedula<<endl;
                	cout<<"\tNombre:   "<<nombre<<" "<<apellido<<endl;
                	cout<<"\tFecha nacimiento: "<<nacimiento<<endl;
                	cout<<"\tCorreo:	"<<correo<<endl;
                	cout<<"\t________________________________\n\n";
               	 
                	//sub menu para opciones de las cuales desea modificar y en bucle para no estar entra y sale..8
               	 
                	cout<<"\tIngresa el nuevo correo del dependiente con la cedula: "<<tempCedula<<"\n\n\t---> ";
                	cin>>tempcorreo;

                	aux<<cedula<<" "<<nombre<<" "<<apellido<<" "<<nacimiento<<" "<<correo<<" "<<PassUsu<<endl;
                	cout<<"\n\n\t\t\tRegistro modificado...\n\t\t\a";
                	}else{
                	aux<<cedula<<" "<<nombre<<" "<<apellido<<" "<<nacimiento<<" "<<correo<<" "<<PassUsu<<endl;
                	}
            	lectura>>cedula;
        	}
	}else{
    	cout<<"\n\tEl archivo no se pudo abrir \n";
	}

	if (encontrado==false){
            	cout<<"\n\tNo se encontro ningun dependiente con la cedula: "<<tempCedula<<"\n\n\t\t\t";
        	}

	aux.close();
	lectura.close();
	remove ("UsuariosN.txt");
	rename("tempUsuario.txt", "UsuariosD.txt");
}

void Deposito(){

	///Variables de la biblioteca fstream para el manejo de archivos
	ofstream escritura2;
	ifstream consulta2;
	
	do{
	escritura2.open("Movimientos.txt", ios::out | ios::app);//crea y escribe, si ya tiene texto une al final del archivo
	consulta2.open("Movimientos.txt", ios::in);//solamente consulta o lee usando la variable sobre el archivo físico 
	
	if (escritura2.is_open() && consulta2.is_open()){
	    	
    	ofstream aux;
		ifstream lectura;
			
		encontrado=false;
		ValidAccion = false;
			
		aux.open("tempUsuario.txt", ios::out);
		lectura.open("UsuariosN.txt", ios::in);
			
		if (aux.is_open() && lectura.is_open()){
			
	    	system("cls");
    		cout<<"\n\tIngrese el usuario al que desea depositar: ";
    		cin>>tempCedula;
    		
			lectura>>cedula;
			
			while (!lectura.eof()){
				
				lectura>>nombre>>apellido>>nacimiento>>correo>>PassUsu>>ctotal;
				
		        if (tempCedula==cedula){
		            encontrado=true;
		            
		        	cout<<"\n\tIngrese la cantidad de dinero que desea depositar a la cuenta a nombre de "<<nombre<<" "<<apellido<<"\n\t ---> ";
		            cin>>temptotal;
		            
					if (temptotal > 0){
						ctotal = ctotal + temptotal;
						aux<<cedula<<" "<<nombre<<" "<<apellido<<" "<<nacimiento<<" "<<correo<<" "<<PassUsu<<" "<<ctotal<<endl;
						system("cls");
	            		cout<<"\n\n\t\tDeposito realizado con exito...";
	            		ValidAccion = true;
	        			}
						else{
						system("cls");
						cout<<"\n\n\t** Ha ingresado un valor incorrecto, reinicie el proceso **";
						system("pause");
						system("cls");
						aux<<cedula<<" "<<nombre<<" "<<apellido<<" "<<nacimiento<<" "<<correo<<" "<<PassUsu<<" "<<ctotal<<endl;
						}
				}else{
					aux<<cedula<<" "<<nombre<<" "<<apellido<<" "<<nacimiento<<" "<<correo<<" "<<PassUsu<<" "<<ctotal<<endl;
					}
				
			
				lectura>>cedula;
			}
		

		}else{
			cout<<"\n\tEl archivo no se pudo abrir \n";
			}
			
		aux.close();
		lectura.close();
		remove ("UsuariosN.txt");
		rename("tempUsuario.txt", "UsuariosN.txt");
		
		if (encontrado==false){
        	cout<<"\n\tNo se encontro ningun usuario con la cedula: "<<tempCedula<<"\n\n\t\t\t";
    		}
    		
		if(ValidAccion == true){	
			fecha = obtenerfecha();
		   	escritura2<<"- "<<tempCedula<<" Deposito "<<temptotal<<" "<<fecha<<endl;
		    cout<<"\tAccion guardada con exito...\n\n\t";
		    system("pause");
		    system("cls");
			}
		
    		
		cout<<"\n\tDesea realizar otro deposito? (S/N): ";
		cin>>opca;
	
		}else{
   			cout<<"El archivo no se pudo abrir \n";
			}
			
		escritura2.close();
		consulta2.close();
		
	}while (opca=='S' or opca=='s');

}

void Retiro(){

	///Variables de la biblioteca fstream para el manejo de archivos
	ofstream escritura2;
	ifstream consulta2;
	
	do{
	escritura2.open("Movimientos.txt", ios::out | ios::app);//crea y escribe, si ya tiene texto une al final del archivo
	consulta2.open("Movimientos.txt", ios::in);//solamente consulta o lee usando la variable sobre el archivo físico 
	
	if (escritura2.is_open() && consulta2.is_open()){
	    	
    	ofstream aux;
		ifstream lectura;
			
		encontrado=false;
		ValidAccion = false;
			
		aux.open("tempUsuario.txt", ios::out);
		lectura.open("UsuariosN.txt", ios::in);
			
		if (aux.is_open() && lectura.is_open()){
			
			system("cls");
    		cout<<"\n\tIngrese el usuario el cual desea retirar dinero: ";
    		cin>>tempCedula;
    		
			lectura>>cedula;
			
			while (!lectura.eof()){
				
				lectura>>nombre>>apellido>>nacimiento>>correo>>PassUsu>>ctotal;
				
		        if (tempCedula==cedula){
		            encontrado=true;
		            
		        	cout<<"\tIngrese la cantidad de dinero que desea retirar a la cuenta de "<<nombre<<" "<<apellido<<"\n\t ---> ";
		            cin>>temptotal;
		            
					if (temptotal <= 0){
						
						system("cls");
						cout<<"\n\n\t** Ha ingresado un valor invalido, reinicie el proceso\n\t\t**";
						system("pause");
						system("cls");
						aux<<cedula<<" "<<nombre<<" "<<apellido<<" "<<nacimiento<<" "<<correo<<" "<<PassUsu<<" "<<ctotal<<endl;
						
	        		}else{
					
					temptotal = (-1*temptotal);
					float checker = ctotal + temptotal;
					
					if (checker < 0){
							
						system("cls");
						cout<<"\n\n\t** El usuario no tiene el saldo suficiente para realizar este retiro **\n\t\t";
						system("pause");
						system("cls");
						aux<<cedula<<" "<<nombre<<" "<<apellido<<" "<<nacimiento<<" "<<correo<<" "<<PassUsu<<" "<<ctotal<<endl;
						
					}else{
						ctotal = checker;
						aux<<cedula<<" "<<nombre<<" "<<apellido<<" "<<nacimiento<<" "<<correo<<" "<<PassUsu<<" "<<ctotal<<endl;
	            		cout<<"\n\n\t\tRetiro realizado con exito...";
	            		ValidAccion = true;
						}
					}
				}else{
					aux<<cedula<<" "<<nombre<<" "<<apellido<<" "<<nacimiento<<" "<<correo<<" "<<PassUsu<<" "<<ctotal<<endl;
					}
				
			
				lectura>>cedula;
			}
		

		}else{
			cout<<"\n\tEl archivo no se pudo abrir \n";
			}
			
		aux.close();
		lectura.close();
		remove ("UsuariosN.txt");
		rename("tempUsuario.txt", "UsuariosN.txt");
		
		if (encontrado==false){
        	cout<<"\n\tNo se encontro ningun usuario con la cedula: "<<tempCedula<<"\n\n\t\t\t";
    		}
    		
		if(ValidAccion == true){	
			fecha = obtenerfecha();
		   	escritura2<<"- "<<tempCedula<<" Retiro "<<temptotal<<" "<<fecha<<endl;
		    cout<<"\n\tAccion guardada con exito...\n\n\t\t";
		    system("pause");
		    system("cls");
			}
		
    	system("cls");
		cout<<"\n\tDesea realizar otro retiro? (S/N): ";
		cin>>opca;
			

		}else{
   			cout<<"El archivo no se pudo abrir \n";
			}
			
		escritura2.close();
		consulta2.close();
		
	}while (opca=='S' or opca=='s');

}

void MenuAccionesD(){

	int opc;

	if (salida){
	inicia_menuAccionesD:
	system("cls");
    
	cout<<"\n\tMenu de acciones";
	cout<<"\n\t1.-Deposito";
	cout<<"\n\t2.-Retiro";
	cout<<"\n\t3.-Salir ";
	
	cout<<"\n\n\tElige una opcion:  ";
    
	cin>>opc;
    
	switch (opc)
    	{
	case 1:{
    	system("cls");
    	Deposito();
    	cout<<"\n\t\t";
    	system ("pause");
    	goto inicia_menuAccionesD;
	}
	case 2:{
    	system("cls");
    	Retiro();
    	cout<<"\n\t\t";
    	system ("pause");
    	goto inicia_menuAccionesD;
	}
	case 3:{
    	cout<<"\n\n\tHa elegido salir...\n\n\t\t"; system ("pause");
    	MenuDependiente();
	}
	
	default:{
    	cout<<"\n\n\tHa elegido una opcion inexistente...\n\n\t\t"; system ("pause");
    	goto inicia_menuAccionesD;
	}
	}//fin switch
    
  }while (opc!=3)
    
    	system("cls");
   	 
}

void MenuUsuario(){

	int opc;

	if (salida){
	inicia_menuUsuario:
	system("cls");
    
	cout<<"\n\tMenu de usuario";
	cout<<"\n\t1.-Crear usuario";
	cout<<"\n\t2.-Iniciar sesion ";
	cout<<"\n\t3.-Salir ";
	
	cout<<"\n\n\tElige una opcion:  ";
    
	cin>>opc;
    
	switch (opc)
    	{
	case 1:{
    	system("cls");
    	AgregarN();
    	cout<<"\n\t\t";
    	system ("pause");
    	goto inicia_menuUsuario;
	}
	case 2:{
    	system("cls");
    	loginU();
    	cout<<"\n\t\t";
    	system ("pause");
    	goto inicia_menuUsuario;
	}
	case 3:{
    	cout<<"\n\n\tHa elegido salir...\n\n\t\t"; system ("pause");
    	MenuPrincipal();
	}
	
	default:{
    	cout<<"\n\n\tHa elegido una opcion inexistente...\n\n\t\t"; system ("pause");
    	goto inicia_menuUsuario;
	}
	}//fin switch
    
  }while (opc!=3)
    
    	system("cls");
    	
   	 
}

void MenuDependiente()
{
	
	int opc;

	if (salida){
	inicia_menuDependiente:
	system("cls");
    
	cout<<"\n\tMenu de dependiente";
	cout<<"\n\t1.-Crear usuario";
	cout<<"\n\t2.-Iniciar sesion ";
	cout<<"\n\t3.-Salir ";
	
	cout<<"\n\n\tElige una opcion:  ";
    
	cin>>opc;
    
	switch (opc)
    	{
	case 1:{
    	system("cls");
    	AgregarD();
    	cout<<"\n\t\t";
    	system ("pause");
    	goto inicia_menuDependiente;
	}
	case 2:{
    	system("cls");
    	loginD();
    	cout<<"\n\t\t";
    	system ("pause");
    	goto inicia_menuDependiente;
	}
	case 3:{
    	cout<<"\n\n\tHa elegido salir...\n\n\t\t"; system ("pause");
    	MenuPrincipal();
	}
	
	default:{
    	cout<<"\n\n\tHa elegido una opcion inexistente...\n\n\t\t"; system ("pause");
    	goto inicia_menuDependiente;
	}
	}//fin switch
    
  }while (opc!=3)
    
    	system("cls");
   	 
}

void MenuAdmin()
{
    
	int opc;

	if (salida){
	inicia_menuAdmin:
	system("cls");
    
	cout<<"\n\tMenu de administrador\n";
	cout<<"\n\t1.-Agregar usuario natural";
	cout<<"\n\t2.-Eliminar usuario natural";
	cout<<"\n\t3.-Lista de usuarios naturales";
	cout<<"\n\t4.-Buscar un usuario natural";
	cout<<"\n\t5.-Modificar usuario natural";
	cout<<"\n\t-----------------------------------";
	cout<<"\n\t6.-Agregar dependiente";
	cout<<"\n\t7.-Eliminar dependiente";
	cout<<"\n\t8.-Lista de dependientes";
	cout<<"\n\t9.-Buscar dependiente";
	cout<<"\n\t10.-Modificar dependiente";
	cout<<"\n\t-----------------------------------";
	cout<<"\n\t11.-Salir al menu principal";
	cout<<"\n\t-----------------------------------";
	cout<<"\n\n\tElige una opcion:  ";
    
	cin>>opc;
    
	switch (opc)
    	{
	case 1:{
    	system("cls");
    	AgregarN();
    	cout<<"\n\t\t";
    	system ("pause");
    	goto inicia_menuAdmin;
	}
	case 2:{
    	system("cls");
    	EliminarN();
    	cout<<"\n\t\t";
    	system ("pause");
    	goto inicia_menuAdmin;
	}
    
	case 3:{
    	system("cls");
    	consultasN();
    	cout<<"\n\t\t";
    	system ("pause");
   	goto inicia_menuAdmin;
	}
	case 4:{
    	system("cls");
    	buscarN();
    	cout<<"\n\t\t";
    	system ("pause");
    	goto inicia_menuAdmin;
	}
	case 5:{
    	system("cls");
    	modificarN();
    	cout<<"\n\t\t";
    	system ("pause");
    
    	goto inicia_menuAdmin;
	}
	case 6:{
    	system("cls");
    	AgregarD();
    	cout<<"\n\t\t";
    	system ("pause");
    
    	goto inicia_menuAdmin;
	}
	case 7:{
    	system("cls");
    	EliminarD();
    	cout<<"\n\t\t";
    	system ("pause");
    	goto inicia_menuAdmin;
	}
	case 8:{
    	system("cls");
    	consultasD();
    	cout<<"\n\t\t";
    	system ("pause");
		goto inicia_menuAdmin;
	}
	case 9:{
    	system("cls");
    	buscarD();
    	cout<<"\n\t\t";
    	system ("pause");
    	goto inicia_menuAdmin;
	}
	case 10:{
    	system("cls");
    	modificarD();
    	cout<<"\n\t\t";
    	system ("pause");
    
    	goto inicia_menuAdmin;
	}
	case 11:{
    	cout<<"\n\n\tHa elegido salir...\n\n\t\t"; system ("pause");
    	salida = 0;
    	MenuPrincipal();
	}
	default:{
    	cout<<"\n\n\tHa elegido una opcion inexistente...\n\n\t\t"; system ("pause");
    	goto inicia_menuAdmin;
	}
	}//fin switch
    
  }while (opc!=11);
    
    	system("cls");
   	 
}

void MenuPrincipal()
{
	int opc;
	salida = 1;
	do{
	system("cls");
    
	cout<<"\n\tBanca en linea Payday\n";
	cout<<"\n\t1.-Administrador";
	cout<<"\n\t2.-Usuario";
	cout<<"\n\t3.-Dependiente";
	cout<<"\n\t4.-Salir";
	cout<<"\n\n\tElige una opcion:  ";
    
	cin>>opc;
    
	switch (opc)
    	{
	case 1:{
   	 
    	string tempUser = "";
    	string tempPass = "";
    	int attempts = 0;
   	 
   	 
    	while (attempts < 3){
       	 
        	if (salida == 1){
       	 
        	system("cls");
        	cout<<"\n\tIngrese el usuario\n";
            	cout<<"\n\n\t->:  ";
        	cin>>tempUser;
       	 
        	system("cls");
        	cout<<"\n\tIngrese la contraseña\n";
        		cout<<"\n\n\t->:  ";
    			char caracter;
				caracter = getch();
				tempPass="";
			while (caracter !=13) { //Lee la contrasenia hasta que se precione el ASCII 13 (ENTER)
	
			if (caracter != 8){	//Condicion para evitar que tome el ASCII 8 (BACKSPACE) como un caracter mas
			tempPass.push_back(caracter);
			cout<<"*"; //Imprime asteriscos para que no se vea la contrasenha 
			} else {
			if (tempPass.length()>0){
				cout<< "\b \b"; //Imprime espacios en blanco para poder borrar con BACKSPACE
				tempPass=tempPass.substr(0, tempPass.length()-1);
				}
			}	
			caracter = getch();
			}

   	 
        	if (tempUser == Admin and tempPass == Password)
        	{
            	MenuAdmin();
            	break;
        	}
                       	 
        	else {
            	attempts = attempts + 1;
            	cout<<"\n\t** Error **\n\tIngrese correctamente el usuario o contraseña";
            	cout<<"\n\tNumero de intentos restantes "<<3-attempts<<"\n\t"; system ("pause");
           	 
            	if (attempts == 3){
                	system ("cls");
                	cout<<"\n\n\t** Numero maximo de intentos superado **\n";
                	break;
                	}
        	}
            	}
        	}    
        	break;
    	}    
case 2:{
    	system("cls");
    	MenuUsuario();
    	cout<<"\n\t\t";
    	system ("pause");
	}
    
	case 3:{
    	system("cls");
    	MenuDependiente();
    	cout<<"\n\t\t";
    	system ("pause");
	}
	case 4:{
    	cout<<"\n\n\tHa elegido salir...\n\n\t\t"; system ("pause");
    	seguir = false;
    	system("cls");
    	exit(0);
	}
	default:{
    	cout<<"\n\n\tHa elegido una opcion inexistente...\n\n\t\t"; system ("pause");
    	system("cls");
    	break;
	}
    	}//fin switch
   	 
    	}while (opc!=4);
    
    	system("cls");
 
    
}

int main()
{
	system ("color 17");
	system ("title Payday");
	setlocale(LC_CTYPE,"Spanish"); // Para usar tildes y "ñ", define idioma
    
	while (seguir){
	MenuPrincipal();
	}
	
	return 0;
}
