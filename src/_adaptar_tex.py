from math import pi
import zipfile
import re

# Unzip arquivos tex
try:
    with zipfile.ZipFile('Introdução_ao_Python_para_Tratamento_de_Dados.zip') as zip_ref:
        zip_ref.extractall('.')
except:
    pass
    
# Tratar    
pacotes = r"""    \usepackage{graphicx}
    \usepackage[brazil]{babel}"""

im_var = r'''tags

    \begin{center}
    \adjustimage{max size={0.5\linewidth}{0.5\paperheight}}{vars_v_objects_4.png}
    \end{center}

    \begin'''

im_slice = r'''Slice Lista

    \begin{center}
    \adjustimage{max size={0.5\linewidth}{0.5\paperheight}}{images.png}
    \end{center}
'''

sumario = r'''    \maketitle

    \tableofcontents  %sumario'''
    
    
greek_dic = {'α' : r'$\alpha$',
             'β' : r'$\beta$',
             'γ' : r'$\gamma$',
             'Γ' : r'$\Gamma$',
             'δ' : r'$\delta$',
             'Δ' : r'$\Delta$',
             'ε' : r'$\epsilon$',
             'ζ' : r'$\zeta$',
             'η' : r'$\eta$',
             'θ' : r'$\teta$',
             'Θ' : r'$\Teta$',
             'ι' : r'$\iota$',
             'κ' : r'$\kappa$',
             'λ' : r'$\lambda$',
             'Λ' : r'$\Lambda$',
             'μ' : r'$\mu$',
             'ν' : r'$\nu$',
             'π' : r'$\pi$',
             'ρ' : r'$\rho$',
             'σ' : r'$\sigma$',
             'Σ' : r'$\Sigma$',
             'τ' : r'$\tau$',
             'φ' : r'$\phi$',
             'Φ' : r'$\Phi$',
             'χ' : r'$\chi$',
             'ψ' : r'$\psi$',
             'Ψ' : r'$\Psi$',
             'ω' : r'$\omega$',
             'Ω' : r'$\Omega$',
            }

with open('Introdução_ao_Python_para_Tratamento_de_Dados.tex', encoding='utf8') as arqin:
    txt = arqin.read()
    txt = txt.replace(r'    \usepackage{graphicx}', pacotes)
    txt = txt.replace(r'\title{Introdução\_ao\_Python\_para\_Tratamento\_de\_Dados}', 
                      r'\title{Introdução ao Python para Tratamento de Dados}\n\author{Hugo Everaldo Salvador Bezerra}')
    txt = txt.replace(r'    \maketitle', sumario)
    txt = txt.replace(r'''tags

    \begin''', im_var)
    txt = txt.replace(r'Slice Lista', im_slice)
    
    txt = re.sub(r'''\\toprule
(& )*\\\\
\\midrule''', r'\\toprule',txt)
    txt.translate(greek_dic)
    

with open('Introducao_ao_Python_para_Tratamento_de_Dados2.tex', 'w', encoding='utf8') as arqout:
    arqout.write(txt)