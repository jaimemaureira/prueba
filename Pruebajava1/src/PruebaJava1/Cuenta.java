
package PruebaJava1;

/**
 *
 * @author Jaime Maureira
 * @05-09-2023
 */
public class Cuenta {
    
    private String nombre, mail;
    private int contrasena;

    public Cuenta() {
    }

    public Cuenta(String nombre, String mail, int contrasena) {
        this.nombre = nombre;
        this.mail = mail;
        this.contrasena = contrasena;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getMail() {
        return mail;
    }

    public void setMail(String mail) {
        this.mail = mail;
    }

    public int getContrasena() {
        return contrasena;
    }

    public void setContrasena(int contrasena) {
        this.contrasena = contrasena;
    }

    @Override
    public String toString() {
        return "Cuenta{" + "nombre=" + nombre + ", mail=" + mail + ", contrasena=" + contrasena + '}';
    }

   
    
    
    
    
}
