import pygame,sys
from pygame.locals import *
import random

class niveles:
    def level_1(self):
        self.ayuda_suma=True 
        self.habilitar_recargar=True
        self.random_start() 

        print self.numero_1,self.numero_2,self.numero_3  

        print "Nivel= "+str(self.level)        

        self.fondo2=pygame.image.load('imagenes/fondo_1.jpg')
        self.ventana.blit(self.fondo2,(0,0))
        pygame.display.flip()

        self.btn_home()
        self.btn_ayuda()  
        self.btn_recargar()     
        self.boton2=pygame.image.load('imagenes/boton2.png')
        self.ventana.blit(self.boton2,(160,250))
        self.ventana.blit(self.boton2,(410,250))
        self.ventana.blit(self.boton2,(655,250))

        imagen_signo_mas=pygame.image.load('imagenes/mas.png')
        self.ventana.blit(imagen_signo_mas,(325,300))
        self.ventana.blit(imagen_signo_mas,(570,300))

        imagen_signo_igual=pygame.image.load('imagenes/=.png')
        self.ventana.blit(imagen_signo_igual,(820,310))


        imagen_ninio=pygame.image.load('imagenes/ninio.png')
        self.ventana.blit(imagen_ninio,(200,50))
    

        #Boton1 seleccionar

        self.boton_selec_1=pygame.image.load('imagenes/estrella_2.png')
        self.ventana.blit(self.boton_selec_1,(280,620))
        self.rect_select = self.boton_selec_1.get_rect()
        self.rect_select.left = 280
        self.rect_select.top = 620

               
       

        #Boton 2 seleccionar
        self.ventana.blit(self.boton_selec_1,(500,620))
        self.rect_select_2=self.boton_selec_1.get_rect()
        self.rect_select_2.left=500
        self.rect_select_2.top=620 
       

        #Boton 3 seleccionar

        self.ventana.blit(self.boton_selec_1,(720,620))
        self.rect_slect_3=self.boton_selec_1.get_rect()
        self.rect_slect_3.left=720
        self.rect_slect_3.top=620 

        #Imprimir texto 
       
        self.imprimir_letra(self.numero_1,(0,0,0),(255,254,234),220,320)
        self.imprimir_letra(self.numero_2,(0,0,0),(255,254,234),480,320)
        self.imprimir_letra(self.numero_3,(0,0,0),(255,254,234),730,320)

        #Imprime el puntaje
        self.imprimir_letra("Puntaje= "+str(self.puntaje),(0,0,0),(255,255,255),390,100)
        self.imprimir_letra("Fallido= "+str(self.fallido),(0,0,0),(255,255,255),390,150)


        # texto_tiempo = pygame.font.SysFont(self.tipo_letra, self.tamanio_letra)                       
        # self.imagenTextoPresent = texto_tiempo.render("Tiempo= "+str(self.tiempo), 
        # True, (0,0,0), (255,255,255) )
        # self.ventana.blit(self.imagenTextoPresent,(390,150))  
        pygame.display.update()        
        self.total=self.numero_1+self.numero_2+self.numero_3
        
        #Random
        resultado=[self.numeros.pop(4),self.numeros.pop(5),self.total]
        random.shuffle(resultado)
        self.result_1=resultado.pop(0)
        self.result_2=resultado.pop(1)
        self.result_3=resultado.pop(0)



        print str(self.result_1),str(self.result_2),str(self.result_3)

        #Imprime las posibles respuestas
        color_resp=198,232,240
        letra_resp_1 = pygame.font.SysFont(self.tipo_letra, self.tamanio_letra)                       
        self.imagenTextoPresent = letra_resp_1.render(str(self.result_1), 
        True, (0,0,0), (color_resp) )
        self.x1_suma=340
        self.Y1_suma=675
        self.ventana.blit(self.imagenTextoPresent,(self.x1_suma,self.Y1_suma))

        self.X2_suma=560
        self.Y2_suma=675
        letra_resp_2 = pygame.font.SysFont(self.tipo_letra, self.tamanio_letra)                       
        self.imagenTextoPresent = letra_resp_2.render(str(self.result_2), 
        True, (0,0,0), (color_resp) )
        self.ventana.blit(self.imagenTextoPresent,(self.X2_suma,self.Y2_suma))

        self.X3_suma=780
        self.Y3_suma=675
        letra_resp_3 = pygame.font.SysFont(self.tipo_letra, self.tamanio_letra)                       
        self.imagenTextoPresent = letra_resp_3.render(str(self.result_3), 
        True, (0,0,0), (color_resp) )

        self.ventana.blit(self.imagenTextoPresent,(self.X3_suma,self.Y3_suma))
        
        pygame.display.update() 
        self.deteccion_click()

    def imagen_ayuda_suma(self):
        self.habilitar_regresar=True
        box=pygame.image.load('imagenes/fondo_ayuda_suma.png')
        self.ventana.blit(box,(0,0))    
        pygame.display.flip()        
        self.btn_regresar(860,90) 
        pygame.display.update()

    def level_resta(self):
        self.random_start()
        self.ayuda_resta=True
        self.habilitar_recargar=True
        print self.numero_1,self.numero_2,self.numero_3  
        self.fondo2=pygame.image.load('imagenes/level_resta.jpg')
        self.ventana.blit(self.fondo2,(0,0))
        pygame.display.flip()
        self.btn_home()
        self.btn_recargar()
        self.btn_ayuda()
        nube_1=pygame.image.load('imagenes/nube_1.png')
        self.rect_nube1=nube_1.get_rect()
        self.rect_nube1.left=50
        self.rect_nube1.top=100
        self.ventana.blit(nube_1,self.rect_nube1)
        print self.rect_nube1

        nube_2=pygame.image.load('imagenes/nube_2.png')
        self.rect_nube2=nube_2.get_rect()
        self.rect_nube2.left=400
        self.rect_nube2.top=100
        self.ventana.blit(nube_2,self.rect_nube2)

        nube_3=pygame.image.load('imagenes/nube_3.png')
        self.rect_nube3=nube_3.get_rect()
        self.rect_nube3.left=680
        self.rect_nube3.top=100
        self.ventana.blit(nube_3,self.rect_nube3)

        # Texto de Suma

        self.imprimir_letra(self.numero_1,(0,0,0),(255,240,1),120,515)
        self.imprimir_letra(self.numero_2,(0,0,0),(255,210,220),390,490)
        self.imprimir_letra(self.numero_3,(0,0,0),(217,247,191),650,480)
        self.imprimir_letra("Puntaje= "+str(self.puntaje),(0,0,0),(122,193,65),995,31)
        self.imprimir_letra("Fallido= "+str(self.fallido),(0,0,0),(122,193,65),1000,80)

        self.total2=self.numero_1-self.numero_2-self.numero_3
        
        if self.total2<=0:
            self.random_start()
            self.level_resta()
        else:
            pass

        self.random_start()    
        resultado_resta=[self.numeros.pop(4),self.numeros.pop(5),self.total2]
        random.shuffle(resultado_resta)
        self.result_1=resultado_resta.pop(0)
        self.result_2=resultado_resta.pop(1)
        self.result_3=resultado_resta.pop(0)

        letra_resp_1 = pygame.font.SysFont(self.tipo_letra, self.tamanio_letra)                       
        self.imagenTextoPresent = letra_resp_1.render(str(self.result_1), 
        True, (0,0,0), (255,255,255) )
        self.X1_resta=180
        self.Y1_resta=150
        self.ventana.blit(self.imagenTextoPresent,(self.X1_resta,self.Y1_resta))

        letra_resp_2 = pygame.font.SysFont(self.tipo_letra, self.tamanio_letra)                       
        self.imagenTextoPresent = letra_resp_2.render(str(self.result_2), 
        True, (0,0,0), (255,255,255) )
        self.X2_resta=465
        self.Y2_resta=140
        self.ventana.blit(self.imagenTextoPresent,(self.X2_resta,self.Y2_resta))

        letra_resp_3 = pygame.font.SysFont(self.tipo_letra, self.tamanio_letra)                       
        self.imagenTextoPresent = letra_resp_3.render(str(self.result_3), 
        True, (0,0,0), (255,255,255) )
        self.X3_resta=800
        self.Y3_resta=160
        self.ventana.blit(self.imagenTextoPresent,(self.X3_resta,self.Y3_resta))




        print str(self.result_1),str(self.result_2),str(self.result_3)        

        pygame.display.update()

    def imagen_ayuda_resta(self):
        self.habilitar_regresar=True
        ayuda_resta=pygame.image.load('imagenes/ayuda_resta.jpg')
        self.ventana.blit(ayuda_resta,(0,0))    
        self.btn_regresar(870,270)        

    def level_mult(self):
        self.random_start() 
        print self.numero_1,self.numero_2,self.numero_3  
        self.fondo2=pygame.image.load('imagenes/fondo_mult.jpg')
        self.ventana.blit(self.fondo2,(0,0))
        pygame.display.flip()
        self.ayuda_mult=True 
        self.habilitar_recargar=True       
        self.btn_home()
        self.btn_recargar()
        self.btn_ayuda()
        self.imprimir_letra(self.numero_1,(0,0,0),(255,255,255),100,355) 
        self.imprimir_letra(self.numero_2,(0,0,0),(255,255,255),540,340)
        

        arbol_1=pygame.image.load('imagenes/arbol_1.png')
        self.rect_arbol_1=arbol_1.get_rect()
        self.rect_arbol_1.left=100
        self.rect_arbol_1.top=560
        self.ventana.blit(arbol_1,self.rect_arbol_1)


        arbol_2=pygame.image.load('imagenes/arbol_2.png')
        self.rect_arbol_2=arbol_2.get_rect()
        self.rect_arbol_2.left=460
        self.rect_arbol_2.top=560
        self.ventana.blit(arbol_2,self.rect_arbol_2)


        arbol_3=pygame.image.load('imagenes/arbol_1.png')
        self.rect_arbol_3=arbol_3.get_rect()
        self.rect_arbol_3.left=850
        self.rect_arbol_3.top=560
        self.ventana.blit(arbol_3,self.rect_arbol_3)

        self.imprimir_letra("Puntaje= "+str(self.puntaje),(0,0,0),(255,255,255),210,120)

        self.imprimir_letra("Fallido= "+str(self.fallido),(0,0,0),(255,255,255),210,165)

        self.total_mult=self.numero_1*self.numero_2

        self.random_start()
        resultado_mult=[self.numeros.pop(4),self.numeros.pop(5),self.total_mult]

        random.shuffle(resultado_mult)
        self.result_1=resultado_mult.pop(0)
        self.result_2=resultado_mult.pop(1)
        self.result_3=resultado_mult.pop(0)



        letra_resp_1 = pygame.font.SysFont(self.tipo_letra, self.tamanio_letra)                       
        self.imagenTextoPresent = letra_resp_1.render(str(self.result_1), 
        True, (0,0,0), (1,124,51) )
        self.X1_mult=250
        self.Y1_mult=640
        self.ventana.blit(self.imagenTextoPresent,(self.X1_mult,self.Y1_mult))

        letra_resp_2 = pygame.font.SysFont(self.tipo_letra, self.tamanio_letra)                       
        self.imagenTextoPresent = letra_resp_2.render(str(self.result_2), 
        True, (0,0,0), (1,124,51) )
        self.X2_mult=525
        self.Y2_mult=630
        self.ventana.blit(self.imagenTextoPresent,(self.X2_mult,self.Y2_mult))


        letra_resp_3 = pygame.font.SysFont(self.tipo_letra, self.tamanio_letra)                       
        self.imagenTextoPresent = letra_resp_3.render(str(self.result_3), 
        True, (0,0,0), (1,124,51) )
        self.X3_mult=980
        self.Y3_mult=630
        self.ventana.blit(self.imagenTextoPresent,(self.X3_mult,self.Y3_mult))

        pygame.display.update()    

    def imagen_ayuda_mult(self):
        self.habilitar_regresar=True
        ayuda_mult=pygame.image.load('imagenes/ayuda_mult.png')
        self.ventana.blit(ayuda_mult,(0,0))
        self.btn_regresar(930,295)            

    def level_divicion(self):

        self.random_start()
        self.num1=self.numero_1+1
        self.num2=self.numero_2+1
        self.ayuda_div=True
        self.habilitar_recargar=True
        self.total_div=(self.num1)/(self.num2)
        print "%s entre %s es %s " % (self.num1,self.num2,self.total_div)                      

        if (self.num1%self.num2)==0:
            print "Es entero"
            self.fondo2=pygame.image.load('imagenes/level_div.jpg')
            self.ventana.blit(self.fondo2,(0,0))
            pygame.display.flip() 

            self.box_div=pygame.image.load("imagenes/box_div.png")
            self.ventana.blit(self.box_div,(370,50))

            self.btn_home()
            self.btn_recargar()
            self.btn_ayuda()
            self.arbol_div_1=pygame.image.load('imagenes/Arbol_div.png')
            self.rect_arbol_div_1=self.arbol_div_1.get_rect()
            self.rect_arbol_div_1.left=117
            self.rect_arbol_div_1.top=580
            self.ventana.blit(self.arbol_div_1,self.rect_arbol_div_1)

            self.arbol_div_2=pygame.image.load('imagenes/Arbol_div.png')
            self.rect_arbol_div_2=self.arbol_div_2.get_rect()
            self.rect_arbol_div_2.left=480
            self.rect_arbol_div_2.top=580
            self.ventana.blit(self.arbol_div_2,self.rect_arbol_div_2)


            self.arbol_div_3=pygame.image.load('imagenes/Arbol_div.png')
            self.rect_arbol_div_3=self.arbol_div_3.get_rect()
            self.rect_arbol_div_3.left=880
            self.rect_arbol_div_3.top=580
            self.ventana.blit(self.arbol_div_3,self.rect_arbol_div_3)

            self.imprimir_letra(self.num1,(255,255,255),(0,0,0),160,320) 
            self.imprimir_letra(self.num2,(255,255,255),(0,0,0),600,335) 

            self.imprimir_letra("Puntaje= "+str(self.puntaje),(0,0,0),(255,255,255),400,65)
            self.imprimir_letra("Fallido= "+str(self.fallido),(0,0,0),(255,255,255),400,115)            
            
            self.random_start()
            self.result_div=[self.numeros[0],self.numeros[1],self.total_div]          

            random.shuffle(self.result_div)
            self.result_div_1=self.result_div[0]
            self.result_div_2=self.result_div[1]
            self.result_div_3=self.result_div[2]

            letra_resp_1 = pygame.font.SysFont(self.tipo_letra, self.tamanio_letra)                       
            self.imagenTextoPresent = letra_resp_1.render(str(self.result_div_1), 
            True, (0,0,0), (116,210,23) )
            self.X1_div=250
            self.Y1_div=640
            self.ventana.blit(self.imagenTextoPresent,(self.X1_div,self.Y1_div))    

            letra_resp_2 = pygame.font.SysFont(self.tipo_letra, self.tamanio_letra)                       
            self.imagenTextoPresent = letra_resp_2.render(str(self.result_div_2), 
            True, (0,0,0), (116,210,23) )
            self.X2_div=595
            self.Y2_div=640
            self.ventana.blit(self.imagenTextoPresent,(self.X2_div,self.Y2_div))   

            letra_resp_3 = pygame.font.SysFont(self.tipo_letra, self.tamanio_letra)                       
            self.imagenTextoPresent = letra_resp_3.render(str(self.result_div_3), 
            True, (0,0,0), (116,210,23) )
            self.X3_div=995
            self.Y3_div=640
            self.ventana.blit(self.imagenTextoPresent,(self.X3_div,self.Y3_div))   


          

        else:
            print "Es decimal"  
            self.level_divicion()         
            
        pygame.display.update()  

    def imagen_ayuda_div(self):
        self.habilitar_regresar=True
        ayuda_div=pygame.image.load('imagenes/ayuda_div.jpg')
        self.ventana.blit(ayuda_div,(0,0))
        self.btn_regresar(911,220)     

class cliked:

    def validacion_home(self):
        if self.rect_home.collidepoint(self.pos):
            print"home"
            self.puntaje=0
            self.fallido=0

            if self.habilitar_level_1:
                self.rect_off(self.rect_select)
                self.rect_off(self.rect_select_2)
                self.rect_off(self.rect_slect_3)

            elif self.habilitar_level_mult: 
                self.rect_off(self.rect_arbol_1)
                self.rect_off(self.rect_arbol_2)
                self.rect_off(self.rect_arbol_3)
            
            elif self.habilitar_level_resta:
                self.rect_off(self.rect_nube1)
                self.rect_off(self.rect_nube2)
                self.rect_off(self.rect_nube3)

            elif self.habilitar_div:
                self.rect_off(self.rect_arbol_div_1)
                self.rect_off(self.rect_arbol_div_2)
                self.rect_off(self.rect_arbol_div_3)    
          

            self.principal()  

    def validacion_ayuda(self):
        if self.rect_ayuda.collidepoint(self.pos):
            print "Ayuda"        
            if self.ayuda_suma:
                print "Suma"
                self.rect_off(self.rect_ayuda)
                self.rect_off(self.rect_home)
                self.rect_off(self.rect_recargar)
                self.rect_off(self.rect_select)
                self.rect_off(self.rect_select_2)
                self.rect_off(self.rect_slect_3)
                self.imagen_ayuda_suma()
            elif self.ayuda_resta:
                print "Resta"
                self.rect_off(self.rect_ayuda)
                self.rect_off(self.rect_home)
                self.rect_off(self.rect_recargar)
                self.rect_off(self.rect_nube1)
                self.rect_off(self.rect_nube2)
                self.rect_off(self.rect_nube3)                
                self.imagen_ayuda_resta()
            elif self.ayuda_mult:
                print "Mult" 
                self.rect_off(self.rect_home)
                self.rect_off(self.rect_ayuda)
                self.rect_off(self.rect_recargar)
                self.rect_off(self.rect_arbol_1)
                self.rect_off(self.rect_arbol_2)
                self.rect_off(self.rect_arbol_3)
                self.imagen_ayuda_mult()
            elif self.ayuda_div:
                print "Div"  
                self.rect_off(self.rect_arbol_div_1)
                self.rect_off(self.rect_arbol_div_2)
                self.rect_off(self.rect_arbol_div_3)
                self.rect_off(self.rect_home)
                self.rect_off(self.rect_recargar)
                self.rect_off(self.rect_ayuda)
                self.imagen_ayuda_div()


    def val_regresar(self):
        if self.rect_regresar.collidepoint(self.pos):
            print "Reg"  
            self.rect_off(self.rect_regresar)
            if self.habilitar_level_1:
                self.level_1() 
            elif self.habilitar_level_resta:
                self.level_resta()  
            elif self.habilitar_level_mult:
                self.level_mult() 
            elif self.habilitar_div:
                self.level_divicion()   

    def val_recargar(self):
        if self.rect_recargar.collidepoint(self.pos):
            print "Recargar"
            self.puntaje=0
            self.fallido=0    
            if self.habilitar_level_1:
                self.level_1()
            elif self.habilitar_level_resta:
                self.level_resta()
            elif self.habilitar_level_mult:
                self.level_mult()
            elif self.habilitar_div:
                self.level_divicion()         
                         
    def seleccion_niveles(self):
        if self.habilitar_seleccion_niveles:
            if self.rect_btn_suma.collidepoint(self.pos):
                print "suma"
                self.sonido_click()
                self.rect_off(self.rect_btn_suma)
                self.rect_off(self.rect_btn_niveles)
                self.rect_off(self.rect_btn_resta)
                self.rect_off(self.rect_btn_mult)
                self.rect_off(self.rect_btn_dividir)
                self.habilitar_level_1=True
                self.habilitar_home=True
                self.habilitar_ayuda=True
                self.level_1() 

            if self.rect_btn_resta.collidepoint(self.pos):
                print "Resta"
                self.sonido_click()
                self.rect_off(self.rect_btn_resta)
                self.rect_off(self.rect_btn_suma)
                self.rect_off(self.rect_btn_dividir)
                self.rect_off(self.rect_btn_mult)
                self.rect_off(self.rect_btn_niveles)
                self.habilitar_level_resta=True
                self.habilitar_home=True
                self.habilitar_ayuda=True
                self.level_resta() 

            if self.rect_btn_mult.collidepoint(self.pos):
                print "Multiplicar"
                self.habilitar_level_mult=True
                self.habilitar_home=True
                self.habilitar_ayuda=True
                self.rect_off(self.rect_btn_suma)
                self.rect_off(self.rect_btn_niveles)
                self.rect_off(self.rect_btn_resta)
                self.rect_off(self.rect_btn_mult)
                self.rect_off(self.rect_btn_dividir)
                self.level_mult()
                self.sonido_click()

            if self.rect_btn_dividir.collidepoint(self.pos):
                print "Dividir" 
                self.sonido_click()  
                self.habilitar_home=True
                self.habilitar_div=True
                self.habilitar_ayuda=True
                self.rect_off(self.rect_btn_suma)
                self.rect_off(self.rect_btn_niveles)
                self.rect_off(self.rect_btn_resta)
                self.rect_off(self.rect_btn_mult)
                self.rect_off(self.rect_btn_dividir)
                self.level_divicion()   

    def validaciones_level_1(self):  

        color_letra_fallido=254,217,216
        if self.rect_select.collidepoint(self.pos):
            print 'colicion2'
            self.sonido_click()
            if self.x1_suma==340 and self.Y1_suma==675:
                
                if self.result_1==self.total:
                    print "Ganastes"
                    self.puntaje+=1
                    self.actializar_puntaje()
                    self.ganar_mover(self.fondo2,self.boton2,self.result_1)
                    pygame.time.wait(self.tiempo_ventana)
                    self.level_1()

                else:
                    print "Perdistes"
                    self.fallido+=1
                    self.imprimir_letra("Fallido= "+str(self.fallido),(0,0,0),(255,255,255),390,150)
                    self.intento_fallido((0,0,0),(color_letra_fallido),'imagenes/estrella_3.png',self.result_1,280,620,340,675)
                    self.sonido_fallido()    
                    pygame.display.update()       
                                                                               
 
        if self.rect_select_2.collidepoint(self.pos):
            self.sonido_click()
            print 'colicion3'
            if self.X2_suma==560 and self.Y2_suma==675:
                if self.result_2==self.total:
                    print "Ganastes"
                    self.puntaje+=1
                    self.actializar_puntaje()
                    self.ganar_mover(self.fondo2,self.boton2,self.result_2)
                    pygame.time.wait(self.tiempo_ventana)
                    self.level_1()

                else:
                    print "Perdistes" 
                    self.fallido+=1
                    self.imprimir_letra("Fallido= "+str(self.fallido),(0,0,0),(255,255,255),390,150)
                    self.intento_fallido((0,0,0),(color_letra_fallido),'imagenes/estrella_3.png',self.result_2,500,620,560,675)
                    self.sonido_fallido()


        if self.rect_slect_3.collidepoint(self.pos):
            print 'coliion4'
            self.sonido_click()  
            if self.X3_suma==780 and self.Y3_suma==675:
                if self.result_3==self.total:
                    print "Ganastes"
                    self.puntaje+=1
                    self.ganar_mover(self.fondo2,self.boton2,self.result_3)
                    self.actializar_puntaje()
                    pygame.time.wait(self.tiempo_ventana)
                    self.level_1()

                else:
                    print "Perdistes"
                    self.fallido+=1
                    self.imprimir_letra("Fallido= "+str(self.fallido),(0,0,0),(255,255,255),390,150)
                    self.intento_fallido((0,0,0),(color_letra_fallido),'imagenes/estrella_3.png',self.result_3,720,620,780,675)
                    self.sonido_fallido()

    def validaciones_level_resta(self):

        if self.rect_nube1.collidepoint(self.pos):
            self.sonido_click()
            print "nube1"
            if self.X1_resta==180 and self.Y1_resta==150:
                if self.result_1==self.total2:
                    print "Ganastes"
                    self.puntaje+=1
                    self.actializar_puntaje()
                    self.intento_fallido((0,0,0),(255,255,255),'imagenes/bueno.png',self.result_1,120,240,180,150)
                    self.imprimir_letra(self.result_1,(0,0,0),(255,240,1),900,490)
                    pygame.time.wait(self.tiempo_ventana)
                    self.level_resta()

                else:
                    print "Perdistes"
                    self.fallido+=1
                    self.imprimir_letra("Fallido= "+str(self.fallido),(0,0,0),(122,193,65),1000,80)
                    self.intento_fallido((0,0,0),(255,255,255),'imagenes/error.png',self.result_1,120,240,180,150)
                    self.sonido_fallido()    
           
        if self.rect_nube2.collidepoint(self.pos):
            self.sonido_click()
            print "nube_2"    
            if self.X2_resta==465 and self.Y2_resta==140:
                if self.result_2==self.total2:
                    print "Ganastes"
                    self.puntaje+=1
                    self.actializar_puntaje()
                    self.intento_fallido((0,0,0),(255,255,255),'imagenes/bueno.png',self.result_2,420,240,465,140)
                    self.imprimir_letra(self.result_2,(0,0,0),(255,240,1),900,490)
                    pygame.time.wait(self.tiempo_ventana)
                    self.level_resta()

                else:
                    print "Perdistes"
                    self.fallido+=1
                    self.intento_fallido((0,0,0),(255,255,255),'imagenes/error.png',self.result_2,420,210,465,140)
                    self.imprimir_letra("Fallido= "+str(self.fallido),(0,0,0),(122,193,65),1000,80)
                    self.sonido_fallido()             
          
        if self.rect_nube3.collidepoint(self.pos):
            print "nube_3"
            self.sonido_click()    
            if self.X3_resta==800 and self.Y3_resta==160:
                if self.result_3==self.total2:
                    print "Ganastes"
                    self.puntaje+=1
                    self.actializar_puntaje()
                    self.intento_fallido((0,0,0),(255,255,255),'imagenes/bueno.png',self.result_3,765,240,800,160)
                    self.imprimir_letra(self.result_3,(0,0,0),(255,240,1),900,490)
                    pygame.time.wait(self.tiempo_ventana)
                    self.level_resta()

                else:
                    print "Perdistes"
                    self.fallido+=1
                    self.intento_fallido((0,0,0),(255,255,255),'imagenes/error.png',self.result_3,765,240,800,160)
                    self.imprimir_letra("Fallido= "+str(self.fallido),(0,0,0),(122,193,65),1000,80)
                    self.sonido_fallido()                 



        pygame.display.update() 

    def validacion_level_mult(self): 
        if self.rect_arbol_1.collidepoint(self.pos):
            print "arbol_1"
            if self.X1_mult==250 and self.Y1_mult==640:
                if self.result_1==self.total_mult:
                    print "Ganas"
                    self.puntaje+=1
                    self.ventana.blit(self.cara_feliz,(220,470))
                    self.intento_fallido((0,0,0),(255,255,255),'imagenes/nube_2.png',self.result_1,930,295,1020,350)
                    # self.imprimir_letra(self.result_1,(0,0,0),(255,255,255),1029,400)
                    pygame.time.wait(self.tiempo_ventana)
                    self.level_mult()
                else:
                    print "Pierdes" 
                    self.fallido+=1
                    self.ventana.blit(self.cara_triste,(220,470))
                    self.imprimir_letra("Fallido= "+str(self.fallido),(0,0,0),(255,255,255),210,165)
                    self.sonido_fallido()   

        if self.rect_arbol_2.collidepoint(self.pos):
            print "arbol_2"
            if self.X2_mult==525 and self.Y2_mult==630:
                if self.result_2==self.total_mult:
                    print "Ganas"
                    self.puntaje+=1
                    self.ventana.blit(self.cara_feliz,(520,470))
                    self.intento_fallido((0,0,0),(255,255,255),'imagenes/nube_2.png',self.result_2,930,295,1020,350)
                    pygame.time.wait(self.tiempo_ventana)
                    self.level_mult()
                else:
                    print "Pierdes"  
                    self.fallido+=1
                    self.ventana.blit(self.cara_triste,(520,470))
                    self.imprimir_letra("Fallido= "+str(self.fallido),(0,0,0),(255,255,255),210,165)
                    self.sonido_fallido()  


        if self.rect_arbol_3.collidepoint(self.pos):

            print "arbol_3"         
            if self.X3_mult==980 and self.Y3_mult==630:
                if self.result_3==self.total_mult:
                    print "Ganas"
                    self.puntaje+=1
                    self.ventana.blit(self.cara_feliz,(995,470))
                    self.intento_fallido((0,0,0),(255,255,255),'imagenes/nube_2.png',self.result_3,930,295,1020,350)
                    pygame.time.wait(self.tiempo_ventana)
                    self.level_mult()
                else:
                    print "Pierdes" 
                    self.fallido+=1
                    self.ventana.blit(self.cara_triste,(955,470))
                    self.imprimir_letra("Fallido= "+str(self.fallido),(0,0,0),(255,255,255),210,165)
                    self.sonido_fallido()     

    def validacion_div(self):
        print "Val level"
        
        self.bicho=pygame.image.load("imagenes/bicho_div.png")
        if self.rect_arbol_div_1.collidepoint(self.pos):
            if self.X1_div==250 and self.Y1_div==640:
                if self.result_div_1==self.total_div:
                    print "Ganas"
                    self.puntaje +=1
                    self.ventana.blit(self.cara_feliz,(224,490))
                    self.ventana.blit(self.bicho,(932,140,0,0))
                    self.imprimir_letra(self.result_div_1,(255,255,255),(0,0,0),1020,310)
                    pygame.time.wait(self.tiempo_ventana)
                    self.level_divicion()
                else:
                    print "Pierdes"
                    self.ventana.blit(self.cara_triste,(224,490))                          
                    self.sonido_fallido()
                    self.fallido+=1
                    self.imprimir_letra("Fallido= "+str(self.fallido),(0,0,0),(255,255,255),400,115)


        elif self.rect_arbol_div_2.collidepoint(self.pos):
            
            if self.X2_div==595 and self.Y2_div==640:
                if self.result_div_2==self.total_div:
                    print "Ganas"
                    self.puntaje +=1
                    self.ventana.blit(self.cara_feliz,(580,490))
                    self.ventana.blit(self.bicho,(932,140,0,0))
                    self.imprimir_letra(self.result_div_2,(255,255,255),(0,0,0),1020,310)
                    pygame.time.wait(self.tiempo_ventana)
                    self.level_divicion()
                else:
                    print "Pierdes"    
                    self.ventana.blit(self.cara_triste,(580,490))                      
                    self.sonido_fallido()
                    self.fallido+=1
                    self.imprimir_letra("Fallido= "+str(self.fallido),(0,0,0),(255,255,255),400,115)                  

        elif self.rect_arbol_div_3.collidepoint(self.pos):
            
            if self.X3_div==995 and self.Y3_div==640:
                if self.result_div_3==self.total_div:
                    print "Ganas"
                    self.puntaje +=1
                    self.ventana.blit(self.cara_feliz,(990,490))
                    self.ventana.blit(self.bicho,(932,140,0,0))    
                    self.imprimir_letra(self.result_div_3,(255,255,255),(0,0,0),1020,310)
                    pygame.time.wait(self.tiempo_ventana)
                    self.level_divicion()
                else:
                    print "Pierdes"     
                    self.sonido_fallido() 
                    self.ventana.blit(self.cara_triste,(990,490))                      
                    self.fallido+=1
                    self.imprimir_letra("Fallido= "+str(self.fallido),(0,0,0),(255,255,255),400,115)    
        pygame.display.update()                
                


CURSOR = (
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  ",
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ",
        "XXX.........................XXXX",
        "XXX..........................XXX",
        "XXX..........................XXX",
        "XXX.........................XXXX",
        "XXX.......XXXXXXXXXXXXXXXXXXXXX ",
        "XXX........XXXXXXXXXXXXXXXXXXX  ",
        "XXX.........XXX                 ",
        "XXX..........XXX                ",
        "XXX...........XXX               ",
        "XXX....X.......XXX              ",
        "XXX....XX.......XXX             ",
        "XXX....XXX.......XXX            ",
        "XXX....XXXX.......XXX           ",
        "XXX....XXXXX.......XXX          ",
        "XXX....XXXXXX.......XXX         ",
        "XXX....XXX XXX.......XXX        ",
        "XXX....XXX  XXX.......XXX       ",
        "XXX....XXX   XXX.......XXX      ",
        "XXX....XXX    XXX.......XXX     ",
        "XXX....XXX     XXX.......XXX    ",
        "XXX....XXX      XXX.......XXX   ",
        "XXX....XXX       XXX.......XXX  ",
        "XXX....XXX        XXX.......XXX ",
        "XXX....XXX         XXX.......XXX",
        "XXX....XXX          XXX......XXX",
        "XXX....XXX           XXX.....XXX",
        "XXX....XXX            XXX...XXXX",
        " XXX..XXX              XXXXXXXX ",
        "  XXXXXX                XXXXXX  ",
        "   XXXX                  XXXX   "
)
