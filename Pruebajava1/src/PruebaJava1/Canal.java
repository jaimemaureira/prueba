
/**
 *
 * @author Jaime maureira
 * @05-09-2023
 */
public class Canal {
    
    private String nombre, mail, descripcion, contacto;
    private int videos, suscriptores;

    public Canal() {
    }

    public Canal(String nombre, String mail, String descripcion, String contacto, int videos, int suscriptores) {
        this.nombre = nombre;
        this.mail = mail;
        this.descripcion = descripcion;
        this.contacto = contacto;
        this.videos = videos;
        this.suscriptores = suscriptores;
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

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }

    public String getContacto() {
        return contacto;
    }

    public void setContacto(String contacto) {
        this.contacto = contacto;
    }

    public int getVideos() {
        return videos;
    }

    public void setVideos(int videos) {
        this.videos = videos;
    }

    public int getSuscriptores() {
        return suscriptores;
    }

    public void setSuscriptores(int suscriptores) {
        this.suscriptores = suscriptores;
    }

    @Override
    public String toString() {
        return "Canal{" + "nombre=" + nombre + ", mail=" + mail + ", descripcion=" + descripcion + ", contacto=" + contacto + ", videos=" + videos + ", suscriptores=" + suscriptores + '}';
    }
    
    public void informacionCanal ()
    
    {
        this.nombre = nombre;
        this.descripcion = descripcion;
    
    }
    
    public void aumentoSuscriptores ()
    {
        this.suscriptores = this.suscriptores ++;
            
    }
            
    public void pago ()
            
    
    
    
}
