import pygame,sys
import random
from pygame.locals import *
from utils import CURSOR , cliked , niveles
import gtk

resolution=(1200,900)


class Main_Class(cliked,niveles):
    rango=10
    level=1
    tiempo_ventana=2000
    ventana=None
    puntaje=0
    fallido=0
    tiempo_aux=1
    tamanio_letra=50
    tipo_letra="Arial"

    def main(self):
        pygame.init()
        # pygame.mixer.music.load('sonidos/musica.ogg')
        # pygame.mixer.music.play(30)
        cursor = pygame.cursors.compile(CURSOR)
        pygame.mouse.set_cursor((32,32), (1,1), * cursor)
        self.ventana=pygame.display.set_mode((resolution))
        pygame.display.set_caption("NicMat")
        self.principal()
        pygame.display.update()    
        
    def principal(self): 
        self.cara_triste=pygame.image.load("imagenes/cara_triste.png")
        self.cara_feliz=pygame.image.load("imagenes/cara_feliz.png")
        self.habilitar_level_1=False
        self.habilitar_level_resta=False
        self.habilitar_div=False
        self.habilitar_seleccion_niveles=False
        self.habilitar_level_mult=False
        self.habilitar_home=False
        self.habilitar_ayuda=False
        self.habilitar_regresar=False
        self.habilitar_recargar=False
        self.ayuda_suma=False
        self.ayuda_resta=False
        self.ayuda_mult=False
        self.ayuda_div=False


        #imagenes
        self.fondo = pygame.image.load('imagenes/principal.jpg')
        self.ventana.blit(self.fondo, (0, 0))
        pygame.display.flip()
            
    
        btn_niveles= pygame.image.load('imagenes/btn_niveles.png')
        self.rect_btn_niveles=btn_niveles.get_rect()
        self.rect_btn_niveles.left=450
        self.rect_btn_niveles.top=600
        self.ventana.blit(btn_niveles,self.rect_btn_niveles)

        pygame.display.update()
         
        
        self.deteccion_click()

    def btn_home(self):
        home=pygame.image.load('imagenes/home.png')
        self.rect_home=home.get_rect()
        self.rect_home.left=30
        self.rect_home.top=30
        self.ventana.blit(home,self.rect_home)    
        pygame.display.update

    def btn_ayuda(self):
        ayuda=pygame.image.load('imagenes/ayuda.png')
        self.rect_ayuda=ayuda.get_rect()
        self.rect_ayuda.left=150
        self.rect_ayuda.top=30
        self.ventana.blit(ayuda,self.rect_ayuda)
        pygame.display.update()    

    def btn_regresar(self,left,top):
        regresar=pygame.image.load('imagenes/iniciar.png')    
        self.rect_regresar=regresar.get_rect()
        self.rect_regresar.left=left
        self.rect_regresar.top=top
        self.ventana.blit(regresar,self.rect_regresar)
        pygame.display.update()

    def btn_recargar(self):
        recargar=pygame.image.load('imagenes/refresh.png')    
        self.rect_recargar=recargar.get_rect()
        self.rect_recargar.left=90
        self.rect_recargar.top=30
        self.ventana.blit(recargar,self.rect_recargar)

    def sonido_click(self):
        sonido_click=pygame.mixer.Sound("sonidos/click.ogg")
        sonido_click.play()
        pygame.time.wait(400)        

    def random_start(self):   
        self.numeros=range(self.rango)
        random.shuffle(self.numeros)
        self.numero_1=self.numeros[0]
        self.numero_2=self.numeros[1]
        self.numero_3=self.numeros[2] 

    def imprimir_letra(self,numero,color,fondo,x,y):  
        texto = pygame.font.SysFont(self.tipo_letra, self.tamanio_letra)                       
        imagenTextoPresent = texto.render(str(numero), 
        True, color, fondo )

        self.ventana.blit(imagenTextoPresent,(x,y))  
        pygame.display.update()

    def intento_fallido(self,color,fondo,ruta,resultado,x,y,x1,y1):
        self.btn_fallido=pygame.image.load(ruta)
        self.ventana.blit(self.btn_fallido,(x,y))
        letra_resp_1 = pygame.font.SysFont(self.tipo_letra, self.tamanio_letra)                       
        self.imagenTextoPresent = letra_resp_1.render(str(resultado), 
        True, color, fondo )
        self.X1=x1
        self.Y1=y1
        self.ventana.blit(self.imagenTextoPresent,(self.X1,self.Y1))
        pygame.display.update()

    def ganar_mover(self,fondo,imagen,respuesta):   
       
        self.ventana.blit(imagen,(900,250))
        texto = pygame.font.SysFont(self.tipo_letra, self.tamanio_letra)                       
        self.imagenTextoPresent = texto.render(str(respuesta), 
        True, (0,0,0), (255,254,234) )
        self.ventana.blit(self.imagenTextoPresent,(960,320))


        pygame.display.update() 

    def sonido_fallido(self):
        self.sonido_error=pygame.mixer.Sound("sonidos/fallido.ogg")
        self.sonido_error.play()

    def rect_off(self,rectangulo):   
        rectangulo.left=0
        rectangulo.top=0
        rectangulo.right=0
        rectangulo.width=0


    def selec_level(self):
        self.fondo_niveles = pygame.image.load('imagenes/niveles.png')
        self.ventana.blit(self.fondo_niveles, (0, 0))
        pygame.display.flip()

        self.btn_suma=pygame.image.load('imagenes/btn_suma.png')
        self.ventana.blit(self.btn_suma,(100,150))
        self.rect_btn_suma=self.btn_suma.get_rect()
        self.rect_btn_suma.left=100
        self.rect_btn_suma.top=150

        self.btn_resta=pygame.image.load('imagenes/btn_resta.png')
        self.ventana.blit(self.btn_resta,(100,380))
        self.rect_btn_resta=self.btn_resta.get_rect()
        self.rect_btn_resta.left=100
        self.rect_btn_resta.top=380

        self.btn_mult=pygame.image.load('imagenes/btn_multiplicar.png')
        self.ventana.blit(self.btn_mult,(500,150))
        self.rect_btn_mult=self.btn_resta.get_rect()
        self.rect_btn_mult.left=500
        self.rect_btn_mult.top=150

        self.btn_dividir=pygame.image.load('imagenes/btn_dividir.png')

        self.ventana.blit(self.btn_dividir,(500,380))
        self.rect_btn_dividir=self.btn_dividir.get_rect()
        self.rect_btn_dividir.left=500
        self.rect_btn_dividir.top=380
        pygame.display.update()

    def actializar_puntaje(self):
        self.tiempo=pygame.time.get_ticks()/1000
        if self.tiempo_aux==self.tiempo:
            self.tiempo_aux+=1


            

    def deteccion_click(self):    
        while True:
            # self.actializar_puntaje()
            while gtk.events_pending():
            	gtk.main_iteration()
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0) 

                if event.type==pygame.MOUSEBUTTONDOWN:
                    self.pos=pygame.mouse.get_pos()
                    print self.pos

                    if self.rect_btn_niveles.collidepoint(self.pos):
                        print "niveles"
                        self.sonido_click()
                       
                        self.selec_level()

                        self.habilitar_seleccion_niveles=True

                    self.seleccion_niveles() 

           
                    if self.habilitar_home:    
                        self.validacion_home()
                    else:
                        pass    
                    
                    if self.habilitar_ayuda:
                        self.validacion_ayuda() 
                    else:
                        pass     

                    if self.habilitar_regresar:
                        self.val_regresar()
                    else:        
                        pass 

                    if self.habilitar_recargar:
                        self.val_recargar()
                    else:
                        pass        

                   
                    if self.habilitar_level_1:  
                        self.validaciones_level_1()
                    else:
                        pass 
                    
                    if self.habilitar_level_resta:     

                        self.validaciones_level_resta()        
                    else:
                        pass   

                    if self.habilitar_level_mult:
                        self.validacion_level_mult()
                    else:
                        pass  
                   
                    if self.habilitar_div:
                        self.validacion_div()
                    else:   
                        pass    

               
if __name__=='__main__':
    Main_Class().main()
