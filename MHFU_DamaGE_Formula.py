
# Multiplicador de Classe.
gs_mc  = 4.8 #Greatsword 
ls_mc  = 4.8 #Longsword 
sns_mc = 1.4 #Sword and Shield
db_mc  = 1.4 #Dual Blades
Hm_mc  = 5.2 #Hammer
hh_mc  = 5.2 #Hunting Horn
lc_mc  = 2.3 #Lance
gl_mc  = 2.3 #Gunlance 
#Multiplicador de Afiação das armas
Vermelho = 0.5
Laranja	 = 0.75
Amarelo	 = 1.0
Verde	 = 1.125
Azul	 = 1.25
Branco	 = 1.3
Roxo     = 1.5
#Bonus elemental de afiação
Elemental_Vermelho = 0.25
Elemental_Laranja  = 0.5
Elemental_Amarelo  = 0.75
Elemental_Verde    = 1.0
Elemental_Azul     = 1.0625
Elemental_Branco   = 1.125
Elemental_Roxo     = 1.2
#Motion Value
gs_mv = 0.48
#dummy
Khezu_defense = 0.7
Khezu_Enraged = 0.9
Khezu_Head    = 0.6




print('\033[1;32m+=+'*20)
print(f'\033[0;36m{"FÓRMULA DO DANO!!":^60}')
print('\033[1;32m+=+'*20)

print('''\033[0;36mMELEE WEAPONS\n
\033[4;36mGreatsword   [1] Hammer       [5]
Longsword    [2] Hunting Horn [6]
SnS          [3] Lance        [7]
Dual Blades  [4] Gunlance     [8]
\n''')

arma=input('\033[0;32mDIGITE O NÚMERO CORRESPONDENTE: ')
if arma == '1':
    #Descrição da arma
    print('''\n\033[0;30mVocê selecionou a Great Sword. Comumente abreviada para GS!
A 'GS' é uma espada gigantesca com um multiplicador de classe de 4.8
''')
    print('\033[4;32m+=+'*20)
    dano=float(input('\n\033[0;31mDANO DA ARMA: '))
    dano_real= dano//4.8
    print('\033[4;32m+=+'*20)
    #Escolha de nível de afiação da arma
    afiação=str(input('''\n\033[0;37mNÍVEL DE AFIAÇÃO DA ARMA\n
\033[31m[Vermelho] \033[33m[Amarelo] \033[32m[Verde] \033[36m[Azul] \033[37m[Branco] \033[35m[Roxo]\n
\033[37mDIGITE A COR CORRESPONDENTE: ''')).capitalize()
    if afiação =='Vermelho':
        afiação=Vermelho
        afi_n='Vermelho'
    elif afiação =='Amarelo':
        afiação=Amarelo
        afi_n='Amarelo'
    elif afiação =='Verde':
        afiação=Verde
        afi_n='Verde'
    elif afiação =='Azul':
        afiação=Azul
        afi_n='Azul'
    elif afiação =='Branco':
        afiação =Branco
        afi_n='Branco'
    elif afiação =='Roxo':
        afiação=Roxo
        afi_n='Roxo'

dano_final= dano_real*gs_mv*afiação*Khezu_Head*Khezu_defense*Khezu_Enraged*1

print('\033[4;32m+=+'*20)

#Módulo
print(f'\n\033[0;33mCOMO EXEMPLO, VAMOS PEGAR SUA ARMA QUE TEM {dano} DE DANO PURO. USANDO DRAW SLASH({gs_mv}) ', end='')
print(f'UMA AFIAÇÃO {afi_n} QUE SUPORTA UM MULTIPLICADOR DE {afiação} VEZES.')
print(f'USAR CONTRA UM KHEZU G-RANK(0.7 defesa) ENRAIVECIDO(0.9 defesa) , ACERTANDO A CABEÇA(60 IMPACTO)')

print('\033[4;32m+=+'*20)
dano_elemental=float(input('\n\033[0;31mDANO ELEMENTAL DA ARMA: '))
dano_elemental_real= dano_elemental//10
print('\033[4;32m+=+'*20)
#Multiplicador de afiação elemental
afiação_elemental=0
if afiação =='Vermelho':
    afiação_elemental=Elemental_Vermelho
elif afiação =='Laranja':
    afiação_elemental=Elemental_Laranja
elif afiação =='Amarelo':
    afiação_elemental=Elemental_Amarelo
elif afiação =='Verde':
    afiação_elemental=Elemental_Verde
elif afiação =='Azul':
    afiação_elemental=Elemental_Azul
elif afiação =='Branco':
    afiação_elemental=Elemental_Branco
elif afiação =='Roxo':
    afiação_elemental=Elemental_Roxo
#Calculo Elemental
dano_elemental_final= dano_elemental_real*afiação_elemental*Khezu_Head*Khezu_defense*Khezu_Enraged
#Resultado
if dano_elemental == 0:
    print(f'\n\033[0;33mO DANO BRUTO DE SUA ARMA É DE {dano_final:.2f}')
else:
    print(f'\n\033[0;33mDANO FINAL BRUTO É DE {dano_final:.2f}.')
    print(f'E O DANO ELEMENTAL É DE {dano_elemental_final}')
