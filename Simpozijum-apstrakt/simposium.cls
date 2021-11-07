% Latex2e class file 


% Latex2e, ver.1996.12
%
\def\fmt@name{info}
\def\fmt@version{2019/05/31}
%
\NeedsTeXFormat{LaTeX2e}[1995/12/01]
\ProvidesClass{simposium}
%              [\fmt@version]
%
\LoadClass{article}
% 
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{float}
\usepackage{times}


\usepackage[T1,OT2]{fontenc}%OT1-latinica, OT2-cirilica
\renewcommand{\rmdefault}{wncyr}%postavljamo font wncyr kao osnovni
\newcommand{\Lat}{\fontencoding{OT1}\fontfamily{cmr}\selectfont}
\def\cyr{\fontencoding{OT2}\fontfamily{wncyr}\selectfont}

\def\zn{,\kern-0.09em,} %navodnik
\newcommand{\navod}[1]{\zn #1"}

\newcommand{\Zh}{\symbol{'021}}
\newcommand{\Ch}{\symbol{'121}}
\newcommand{\Sh}{\symbol{'130}}
\newcommand{\Cc}{\symbol{'007}}
\newcommand{\Dj}{\symbol{'006}}
\newcommand{\Dd}{\symbol{'002}}
\newcommand{\Lj}{\symbol{'001}}
\newcommand{\Nj}{\symbol{'000}}

\newcommand{\zh}{\symbol{'031}}
\newcommand{\ch}{\symbol{'161}}
\newcommand{\sh}{\symbol{'170}}
\newcommand{\cc}{\symbol{'017}}
\renewcommand{\dj}{\symbol{'016}}
\newcommand{\dd}{\symbol{'012}}
\newcommand{\lj}{\symbol{'011}}
\newcommand{\nj}{\symbol{'010}}

%\def\dj{\mbox{d\kern-0.32em\raise0.65ex\hbox{-}}}%{d\kern-0.6em\char"16\kern-0.1em}%
%\def\Dj{\mbox{\raise0.3ex\hbox{-}\kern-0.4em D}}


\theoremstyle{plain}


\DeclareOption{eng}{
	\renewcommand{\encodingdefault}{OT1}
	\renewcommand{\rmdefault}{cmr}
	\gdef\@journal{Symposium MATHEMATICS AND APPLICATION, Faculty of Mathematics, University of Belgrade}
	
	\newtheorem{theorem}{Theorem}
	\newtheorem{corollary}{Corollary}
	\newtheorem{lemma}{Lemma}
	\newtheorem{proposition}{Proposition}
	\theoremstyle{definition}
	\newtheorem{definition}{Definition}
	\theoremstyle{remark}
	\newtheorem{remark}{Remark}
	\newtheorem*{notation}{Notation}
	
	\theoremstyle{example}
	\newtheorem{example}{Example}
	\theoremstyle{exercise}
	\newtheorem{exercise}{Exercise}
	\theoremstyle{problem}
	\newtheorem{problem}{Problem}
	\newtheorem*{acknowledgements}{Acknowledgements}
	\newenvironment{solution}{\renewcommand{\proofname}{Solution}\renewcommand{\qedsymbol}{$\triangle$}\begin{proof}}
	{\end{proof}}
    \newcommand\bibname{References}%
    \renewcommand\figurename{Figure}
    \renewcommand\tablename{Table}
    \renewcommand\appendixname{APPENDIX}
    \renewcommand\abstractname{Abstract.}
    \newcommand\keywordsname{Keywords}
}


\DeclareOption{lat}{	
	\renewcommand{\encodingdefault}{OT1}
	\renewcommand{\rmdefault}{cmr}
	
	\gdef\@journal{{ Simpozijum MATEMATIKA I PRIMENE, Matemati\v cki fakultet, Univerzitet u Beogradu}}
	
	\renewcommand\abstractname{Apstrakt.}
	\newcommand\bibname{Bibliografija}%
	\renewcommand\figurename{Slika}
	\renewcommand\tablename{Tabela}
	\renewcommand\appendixname{APENDIKS}
	\newcommand\keywordsname{Klju\v cne re\v ci}
	\newenvironment{solution}{\renewcommand{\proofname}{{ Re\v s{}enje}}\renewcommand{\qedsymbol}{$\triangle$}\begin{proof}}
		{\end{proof}}
	\renewcommand{\proofname}{{Dokaz}}
	%%%%%%
	\newtheorem{theorem}{{ Teorema}}
	\newtheorem{corollary}{{ Posledica}}
	\newtheorem{lemma}{{ Lema}}
	\newtheorem{proposition}{{ Tvr\dj enje}}
	\theoremstyle{definition}
	\newtheorem{definition}{{ Definicija}}
	\theoremstyle{remark}
	\newtheorem{remark}{{ Napomena}}
	\newtheorem*{notation}{{ Notacija}}
	
	\theoremstyle{example}
	\newtheorem{example}{{ Primer}}
	\theoremstyle{exercise}
	\newtheorem{exercise}{{ Zadatak}}
	\theoremstyle{problem}
	\newtheorem{problem}{{ Problem}}
	\newtheorem*{acknowledgements}{{ Zahvalnica}}
}



\DeclareOption{cyr}{	
	\gdef\@journal{{ Simpozijum MATEMATIKA I PRIMENE, Matemati\ch ki fakultet, Univerzitet u Beogradu}}
	
	\renewcommand\abstractname{Apstrakt.}
	\newcommand\bibname{Bibliografija}%
	\renewcommand\figurename{Slika}
	\renewcommand\tablename{Tabela}
	\renewcommand\appendixname{APENDIKS}
	\newcommand\keywordsname{Klju\ch ne re\ch i}
	\newenvironment{solution}{\renewcommand{\proofname}{{ Re\sh{}enje}}\renewcommand{\qedsymbol}{$\triangle$}\begin{proof}}
		{\end{proof}}
	\renewcommand{\proofname}{{Dokaz}}
	%%%%%%
	\newtheorem{theorem}{{ Teorema}}
	\newtheorem{corollary}{{ Posledica}}
	\newtheorem{lemma}{{ Lema}}
	\newtheorem{proposition}{{ Tvrdjenje}}
	\theoremstyle{definition}
	\newtheorem{definition}{{ Definicija}}
	\theoremstyle{remark}
	\newtheorem{remark}{{ Napomena}}
	\newtheorem*{notation}{{ Notacija}}
	
	\theoremstyle{example}
	\newtheorem{example}{{ Primer}}
	\theoremstyle{exercise}
	\newtheorem{exercise}{{ Zadatak}}
	\theoremstyle{problem}
	\newtheorem{problem}{{ Problem}}
	\newtheorem*{acknowledgements}{{ Zahvalnica}}
}



\renewcommand\@ptsize{}
\newif\if@restonecol
\newif\if@titlepage
\@titlepagetrue
\newif\if@openright
\newif\if@mainmatter \@mainmattertrue
% Page dimension
\setlength\paperheight {297mm}%
\setlength\paperwidth  {210mm}
\DeclareOption{landscape}
   {\setlength\@tempdima   {\paperheight}%
    \setlength\paperheight {\paperwidth}%
    \setlength\paperwidth  {\@tempdima}}
% Font dimensions




\DeclareOption{draft}{\setlength\overfullrule{5pt}}
\DeclareOption{final}{\setlength\overfullrule{0pt}}
\DeclareOption{titlepage}{\@titlepagetrue}
\DeclareOption{notitlepage}{\@titlepagefalse}
\DeclareOption{openright}{\@openrighttrue}
\DeclareOption{openany}{\@openrightfalse}
\DeclareOption{onecolumn}{\@twocolumnfalse}
\DeclareOption{twocolumn}{\@twocolumntrue}
\DeclareOption{leqno}{\input{leqno.clo}}
\DeclareOption{fleqn}{\input{fleqn.clo}}
%
% Numbering switches:
\newif\if@seceqn   \@seceqnfalse   \DeclareOption{seceqn}{\@seceqntrue}
\newif\if@secfloat \@secfloatfalse \DeclareOption{secfloat}{\@secfloattrue}
\newif\if@secthm                   \DeclareOption{secthm}{\@secthmtrue}
\newif\if@nameyear \@nameyearfalse \DeclareOption{nameyear}{\global\@nameyeartrue}
\DeclareOption{number}{\global\@nameyearfalse}
%
\DeclareOption{pagframe}{}
%

\ExecuteOptions{10pt,twoside,onecolumn,finall}%,openany}%}%
\ProcessOptions
%
%************************* FONTS
\def\@xivpt{14}
\def\@xviipt{17}
\def\@xviiipt{18}
\def\@xxpt{20}
\def\@xxivpt{24}

\renewcommand\normalsize{%
   \@setfontsize\normalsize\@xpt{12pt plus .1pt minus .1pt}%
   \abovedisplayskip 12\p@ \@plus2\p@ \@minus2\p@%12
   \abovedisplayshortskip \z@ \@plus3\p@
   \belowdisplayshortskip 6\p@ \@plus2\p@
   \belowdisplayskip \abovedisplayskip
   \let\@listi\@listI}
\normalsize

\renewcommand\small{%
   \@setfontsize\small\@ixpt{11}%
   \abovedisplayskip 11\p@ \@plus2\p@
   \abovedisplayshortskip \z@ \@plus2\p@
   \belowdisplayshortskip 5\p@ \@plus2\p@
   \def\@listi{\leftmargin\leftmargini
               \topsep 4\p@ \@plus2\p@ \@minus2\p@
               \parsep 2\p@ \@plus\p@ \@minus\p@
               \itemsep \parsep}%
   \belowdisplayskip \abovedisplayskip
}
\renewcommand\footnotesize{%
   \@setfontsize\footnotesize\@viiipt\@xpt%
   \abovedisplayskip 10\p@ \@plus2\p@ \@minus2\p@
   \abovedisplayshortskip \z@ \@plus\p@
   \belowdisplayshortskip 5\p@ \@plus\p@
   \def\@listi{\leftmargin\leftmargini
               \topsep 3\p@ \@plus\p@ \@minus\p@
               \parsep 2\p@ \@plus\p@ \@minus\p@
               \itemsep \parsep}%
   \belowdisplayskip \abovedisplayskip
}
\renewcommand\scriptsize{\@setfontsize\scriptsize\@viipt\@viiipt}
\renewcommand\tiny{\@setfontsize\tiny\@vipt\@viipt}
\renewcommand\large{\@setfontsize\large\@xiipt{14}}
\renewcommand\Large{\@setfontsize\Large\@xivpt{16}}
\renewcommand\LARGE{\@setfontsize\LARGE\@xviiipt{20}}
\renewcommand\huge{\@setfontsize\huge\@xxpt{26}}
\renewcommand\Huge{\@setfontsize\Huge\@xxivpt{26}}

% Customization of fonts
\renewcommand\sldefault{it}
\renewcommand\bfdefault{b}
\let\slshape\itshape
%
% ********************* DIMENSIONS:
% TEXT DIMENSIONS
\setlength\parindent{1.5pc}
%\setlength\textwidth{26pc}
\setlength\textwidth{158mm}%{113mm}
\setlength\textheight{54\baselineskip} %48
\addtolength\textheight{\topskip}
\setlength\columnsep{2pc}
\setlength\columnwidth{18pc}
\setlength\columnseprule{0\p@}
%\hoffset -1in
\voffset -0.7in%-0.3in
% HEADS:
\setlength\headheight{12\p@}
\setlength\headsep   {24\p@}
\setlength\topskip   {18\p@}
\setlength\footskip  {24\p@}
\setlength\maxdepth  {.5\topskip}
% SIDE MARGINS
\setlength\oddsidemargin  {2mm}
\setlength\evensidemargin {2mm}%{15mm}148-113-20=15mm 210-165-20=25
\setlength\topmargin      {5pt}%5
% TEXT PARAMETERS
\setlength\lineskip{1\p@}
\setlength\normallineskip{1\p@}
\renewcommand\baselinestretch{}
\setlength\parskip{0\p@}
%
% BREAKS
\setlength\smallskipamount{3\p@ \@plus 1\p@ \@minus 1\p@}
\setlength\medskipamount{6\p@ \@plus 2\p@ \@minus 1\p@}
\setlength\bigskipamount{12\p@ \@plus 4\p@ \@minus 2\p@}
\def\Bigskipamount{18\p@ \@plus 6\p@ \@minus 2\p@}
% PAGE-BREAKING PENALTIES
\clubpenalty=4000
\widowpenalty=4000
\displaywidowpenalty=50
\predisplaypenalty=10000   % Breaking before a math display.
% \postdisplaypenalty  % Breaking after a math display.
% \interlinepenalty    % Breaking at a line within a paragraph.
% \brokenpenalty       % Breaking after a hyphenated line.
\tolerance=1600
\hbadness=1600
%
%
\if@twocolumn
 \setlength\marginparsep {10\p@}
\else
  \setlength\marginparsep{7\p@}
\fi
\setlength\marginparpush{5\p@}

% FOOTNOTES
\setlength\footnotesep{6.65\p@}
\setlength{\skip\footins}{12\p@ \@plus 6\p@}
% FLOATS
\setlength\floatsep    {15\p@ \@plus 6\p@ \@minus 2\p@}
\setlength\textfloatsep{18\p@ \@plus 6\p@ \@minus 6\p@}
\setlength\intextsep   {15\p@ \@plus 2\p@ \@minus 2\p@}
\setlength\dblfloatsep    {15\p@ \@plus 2\p@ \@minus 2\p@}
\setlength\dbltextfloatsep{30\p@ \@plus 6\p@ \@minus 18\p@}
%  For floats on a separate float page or column:
\setlength\@fptop{0\p@ \@plus 1fil}
\setlength\@fpsep{8\p@ \@plus 1000fil}
\setlength\@fpbot{0\p@ \@plus 1fil}
\setlength\@dblfptop{0\p@ \@plus 1fil}
\setlength\@dblfpsep{8\p@ \@plus 1000fil}
\setlength\@dblfpbot{0\p@ \@plus 1fil}
%
\setcounter{topnumber}{5}
\renewcommand\topfraction{.90}
\setcounter{bottomnumber}{5}
\renewcommand\bottomfraction{.90}
\setcounter{totalnumber}{10}
\renewcommand\textfraction{.10}
\renewcommand\floatpagefraction{.9}
\setcounter{dbltopnumber}{5}
\renewcommand\dbltopfraction{.99}
\renewcommand\dblfloatpagefraction{.8}
%
% PENALTIES
\@lowpenalty   51
\@medpenalty  151
\@highpenalty 301
\@beginparpenalty -\@lowpenalty
\@endparpenalty   -\@lowpenalty
\@itempenalty     -\@lowpenalty
% LISTS
\setlength\partopsep{0\p@}
\def\@listi{\leftmargin\leftmargini
            \parsep 4\p@ \@plus2\p@ \@minus\p@
            \topsep 8\p@ \@plus2\p@ \@minus4\p@
            \itemsep4\p@ \@plus2\p@ \@minus\p@}
\let\@listI\@listi
\@listi
\def\@listii {\leftmargin\leftmarginii
              \labelwidth\leftmarginii
              \advance\labelwidth-\labelsep
              \topsep    4\p@ \@plus2\p@ \@minus\p@
              \parsep    2\p@ \@plus\p@  \@minus\p@
              \itemsep   \parsep}
\def\@listiii{\leftmargin\leftmarginiii
              \labelwidth\leftmarginiii
              \advance\labelwidth-\labelsep
              \topsep    2\p@ \@plus\p@\@minus\p@
              \parsep    \z@
              \partopsep \p@ \@plus\z@ \@minus\p@
              \itemsep   \topsep}
\def\@listiv {\leftmargin\leftmarginiv
              \labelwidth\leftmarginiv
              \advance\labelwidth-\labelsep}
\def\@listv  {\leftmargin\leftmarginv
              \labelwidth\leftmarginv
              \advance\labelwidth-\labelsep}
\def\@listvi {\leftmargin\leftmarginvi
              \labelwidth\leftmarginvi
              \advance\labelwidth-\labelsep}
%
% ******************** HEADINGS
\def\leftrh#1{\gdef\leftmark{#1}}   \let\leftmark\relax
\def\rightrh#1{\gdef\rightmark{#1}} \let\rightmark\relax
\let\runningauthor\leftrh
\let\runningtitle\rightrh
\def\etal{et al.}
%
% Normalus RH
\def\ps@headings{%
      \let\@oddfoot\@empty\let\@evenfoot\@empty
      \def\@evenhead{\small\rlap{\thepage}\hfill\textrm{\leftmark}\hfill}%\textit  keiciu i \textrm????/
      \def\@oddhead{\small\hfill\textrm{\rightmark}\hfill\llap{\thepage}}%\textit????
}%
% Tuscias RH
\def\ps@empty{\let\@mkboth\@gobbletwo
     \def\@oddhead{\hfill}\def\@oddfoot{}
\let\@evenhead\@oddhead\let\@evenfoot\@oddfoot}
%
% RH  su puslapio numeriu apacioje
\def\ps@plain{\let\@mkboth\@gobbletwo
     \def\@oddhead{\hfill}\def\@oddfoot{}
\let\@evenhead\@oddhead
  \def\@oddfoot{\hfill\small\thepage\hfill}
  \let\@evenfoot\@oddfoot
}
% Copyright RH
\def\ps@copyright{\let\@mkboth\@gobbletwo\vskip 48pt
%     \def\@oddhead{\footnotesize\@copyright\hfill}\def\@oddfoot{}
      \def\@oddhead{\hfill\@copyright}\def\@oddfoot{}
\let\@evenhead\@oddhead\let\@evenfoot\@oddfoot}
% COPYRIGHT
\def\@copyright{%
{\footnotesize \@journal, \the\@pubyear\  \Lat{\@volume} \@issue}} 
%\@journal \the\@pubyear\  \@issue \@pagerange}
% ************************ FOOTNOTE
\renewcommand\footnoterule{%
  \kern-3\p@
  \hrule\@width12pc
  \kern2.6\p@}
\renewcommand\@makefntext[1]{%
    \parindent 1.5pc\@makefnmark #1}
\def\@makefnmark{\@textsuperscript{\normalfont\@thefnmark}}%
%
% ************************ Counters
\setcounter{secnumdepth}{4}
%\newcounter {section}
%\newcounter {subsection}[section]
%\newcounter {subsubsection}[subsection]
%\newcounter {paragraph}[subsubsection]
%\newcounter {subparagraph}[paragraph]
\renewcommand\thesection {\@arabic\c@section}
\renewcommand\thesubsection   {\thesection.\@arabic\c@subsection}
\renewcommand\thesubsubsection{\thesubsection .\@arabic\c@subsubsection}
\renewcommand\theparagraph    {\thesubsubsection.\@arabic\c@paragraph}
\renewcommand\thesubparagraph {\theparagraph.\@arabic\c@subparagraph}
%
% ******************** Sectioning commands
\def\no@harm{\let\thanks=\@gobble \let\\=\@empty}
%**************** Section commands
\def\nohyphen{\pretolerance=10000 \tolerance=10000
\hyphenpenalty=10000 \exhyphenpenalty=10000}
\renewcommand\section{\@startsection {section}{1}{0pt}%{1.5pc}%
                                   {\bigskipamount}%
                                   {\medskipamount}%{0.5em}%{-0.5em}
                                   {\bfseries}}
\renewcommand\subsection{\@startsection {subsection}{2}{0pt}%{1.5pc}%
                                   {\medskipamount}%
                                   {0.5em}%{-0.5em}
                                   {\bfseries}}
\renewcommand\subsubsection{\@startsection{subsubsection}{3}{0pt}%{1.5pc}%
                                     {-\smallskipamount}%
                                     {0.5em}%{-0.5em}
                                     {\bfseries\itshape}}
\renewcommand\paragraph{\@startsection{paragraph}{4}{1.5pc}%
                                    {1pt}%
                                    {-0.5em}%
                                    {\bfseries}}
\renewcommand\subparagraph{\@startsection{subparagraph}{5}{1.5pc}%
                                       {\medskipamount}%
                                       {-.5em}%
                                      {\normalsize\sffamily}}
% Format for the counter:
\def\@seccntformat#1{\csname the#1\endcsname.\enspace}
%
%****************** LISTS
\if@twocolumn
  \setlength\leftmargini  {2em}
\else
  \setlength\leftmargini  {2.5em}
\fi
\leftmargin  \leftmargini
\setlength\leftmarginii  {2.2em}
\setlength\leftmarginiii {1.87em}
\setlength\leftmarginiv  {1.7em}
\if@twocolumn
  \setlength\leftmarginv  {.5em}
  \setlength\leftmarginvi {.5em}
\else
  \setlength\leftmarginv  {1em}
  \setlength\leftmarginvi {1em}
\fi
\setlength  \labelsep  {.5em}
\setlength  \labelwidth{\leftmargini}
\addtolength\labelwidth{-\labelsep}
\renewcommand\theenumi{\@arabic\c@enumi}
\renewcommand\theenumii{\@alph\c@enumii}
\renewcommand\theenumiii{\@roman\c@enumiii}
\renewcommand\theenumiv{\@Alph\c@enumiv}
\renewcommand\labelenumi{\theenumi.}
\renewcommand\labelenumii{(\theenumii)}
\renewcommand\labelenumiii{\theenumiii.}
\renewcommand\labelenumiv{\theenumiv.}
\renewcommand\p@enumii{\theenumi}
\renewcommand\p@enumiii{\theenumi(\theenumii)}
\renewcommand\p@enumiv{\p@enumiii\theenumiii}
%
\def\setenumlabel#1{\gdef\max@enumlabel{#1}}
\setenumlabel{1.}
%
\def\setenumtype#1{%
\if#1a \let\enumerate\enumeratea\fi%
\if#1b \let\enumerate\enumerateb\fi%
\if#1c \let\enumerate\enumeratec\fi%
}
%
% ENUMERATE type A:
%   (iii) xxx xxx
% xxx xxx
\def\enumeratea{\@ifnextchar[{\enumerate@a}{\enumerate@a[\max@enumlabel]}}

\def\enumerate@a[#1]{\ifnum \@enumdepth >4 \@toodeep\else
 \advance\@enumdepth \@ne
 \edef\@enumctr{enum\romannumeral\the\@enumdepth}%
 \list {\csname label\@enumctr\endcsname}%
 {\usecounter{\@enumctr}\def\makelabel##1{{\hfill\rm ##1}}
\settowidth{\labelwidth}{#1}
\advance\labelwidth by\parindent \labelsep=0.5em
 \leftmargin\z@ \rightmargin\z@ \itemindent=\labelwidth
        \advance\itemindent\labelsep
        \partopsep\z@ \topsep\z@ \parsep\z@ \itemsep\z@
 \listparindent\z@}\fi\setenumlabel{1.}}
%
% % ENUMERATE type B:
%   (iii) xxx xxx
%         xxx xxx
\def\enumerateb{\@ifnextchar[{\enumerate@b}{\enumerate@b[\max@enumlabel]}}
%
\def\enumerate@b[#1]{\ifnum \@enumdepth >4 \@toodeep\else
 \advance\@enumdepth \@ne
 \edef\@enumctr{enum\romannumeral\the\@enumdepth}%
 \list {\csname label\@enumctr\endcsname}%
 {\usecounter{\@enumctr}\def\makelabel##1{{\hfill\rm ##1}}
\settowidth{\labelwidth}{#1}
\advance\labelwidth by\parindent \labelsep=0.5em
 \leftmargin\z@ \rightmargin\z@ \itemindent=\labelwidth
        \advance\itemindent\labelsep
        \leftmargin=\the\itemindent\itemindent=\z@
        \partopsep\z@ \topsep\z@ \parsep\z@ \itemsep\z@ \@rightskip\z@ plus 1fil
 \listparindent\z@}\fi\setenumlabel{1.}}
%
%  ENUMERATE type C:
% 1.  xxx xxx
%     xxx xxx
\def\enumeratec{\@ifnextchar[{\enumerate@c}{\enumerate@c[\max@enumlabel]}}
\def\enumerate@c[#1]{\ifnum \@enumdepth >4 \@toodeep\else
 \advance\@enumdepth \@ne
 \edef\@enumctr{enum\romannumeral\the\@enumdepth}%
 \list {\csname label\@enumctr\endcsname}%
 {\usecounter{\@enumctr}\def\makelabel##1{{\hfill\rm ##1}}
\settowidth{\labelwidth}{#1} %\advance\labelwidth by\parindent
 \labelsep=0.5em
 \leftmargin\z@ \rightmargin\z@ \itemindent=\labelwidth
        \advance\itemindent\labelsep
        \leftmargin=\the\itemindent\itemindent=\z@
        \partopsep\z@ \topsep\z@ \parsep\z@ \itemsep\z@ \@rightskip\z@ plus 1fil
 \listparindent\z@}\fi\setenumlabel{1.}}
%
\setenumtype{a}
% ENUMERATE pabaiga
%%%%%%%%%%%%%%%%%%%%%% ITEMIZE
\renewcommand\labelitemi{$\bullet$}
\renewcommand\labelitemii{\normalfont\bfseries \textendash}
\renewcommand\labelitemiii{\textasteriskcentered}
\renewcommand\labelitemiv{\textperiodcentered}

% Bendras saraso atitraukimas
\let\@itemize@indent\parindent
%
\def\setitemtype#1{%
\if#1a \let\itemize\itemizea\fi%
\if#1c \let\itemize\itemizec\fi%
}

% Itemize a
%  x text text text
% text text text
\def\itemizea{\@ifnextchar[{\itemize@a}{\itemize@a[]}}
\def\itemize@a[#1]{\ifnum \@itemdepth >4 \@toodeep\else
  \advance\@itemdepth \@ne
  \edef\@itemitem{labelitem\romannumeral\the\@itemdepth}%
  \if.#1. \else\def\@@tempa{#1}\edef\@itemitem{@@tempa}\fi\list
{\csname\@itemitem\endcsname}{\settowidth{\labelwidth}
                {\csname\@itemitem\endcsname}
                \def\makelabel##1{##1\hfill}\labelsep=0.5em%ST
		\itemindent=\labelwidth \advance\itemindent\labelsep
                \advance\itemindent\@itemize@indent
		\leftmargin\z@ \rightmargin\z@ %\itemindent=\z@
                \partopsep\z@ \topsep12pt \parsep\z@
		\itemsep\z@ \listparindent\z@} \fi}

% Itemize c
% x text text text
%   text text text
%
\def\itemizec{\@ifnextchar[{\itemize@c}{\itemize@c[]}}
\def\itemize@c[#1]{\ifnum \@itemdepth >4 \@toodeep\else
  \advance\@itemdepth \@ne
  \edef\@itemitem{labelitem\romannumeral\the\@itemdepth}%
  \if.#1. \else\def\@@tempa{#1}\edef\@itemitem{@@tempa}\fi\list
{\csname\@itemitem\endcsname}{\settowidth{\labelwidth}
                {\csname\@itemitem\endcsname}
                \def\makelabel##1{##1}\labelsep=0.5em%ST
		\itemindent=\labelwidth \advance\itemindent\labelsep
                \advance\itemindent\@itemize@indent
		\leftmargin\the\itemindent \itemindent=\z@
                \partopsep\z@ \topsep6pt \parsep\z@ \@rightskip\z@ plus 1fil
		\itemsep\z@ \listparindent\z@} \fi}

\let\itemize\itemizec
% ITEMIZE pabaiga

\renewenvironment{description}
               {\list{}{\labelwidth\z@ \itemindent-\leftmargin
                        \let\makelabel\descriptionlabel}}
               {\endlist}
\renewcommand*\descriptionlabel[1]{\hspace\labelsep
                                \normalfont\bfseries #1}
\renewenvironment{verse}
               {\let\\\@centercr
                \list{}{\itemsep      \z@
                        \itemindent   -1.5em%
                        \listparindent\itemindent
                        \rightmargin  \leftmargin
                        \advance\leftmargin 1.5em}%
                \item\relax}
               {\endlist}

\renewenvironment{quotation}
               {\list{}{\footnotesize\listparindent 1.5pc%
                        \itemindent    \listparindent%
                        \rightmargin 2pc   \leftmargin 2pc%
                        \partopsep\z@ \topsep6pt \parsep\z@%
                        }%
                \item[\Q@strut]\relax}
               {\endlist}
\def\Q@strut{\leavevmode\hbox{\vrule height9pt depth1pt width0pt}}

\renewenvironment{quote}
               {\list{}{\footnotesize\listparindent\z@%
                        \itemindent    \listparindent%
                        \rightmargin 2pc   \leftmargin 2pc%
                        \partopsep\z@ \topsep6pt \parsep\z@%
                        }%
                \item[\Q@strut]\relax}
               {\endlist}
%
%************************** MATH SETTINGS
\setlength\arraycolsep{2\p@}
\setlength\tabcolsep{6\p@}
\setlength\arrayrulewidth{.5\p@}
\setlength\doublerulesep{2\p@}
\setlength\tabbingsep{\labelsep}
\skip\@mpfootins = \skip\footins
\setlength\fboxsep{3\p@}
\setlength\fboxrule{.4\p@}
\if@seceqn
\@addtoreset {equation}{section}
\renewcommand\theequation{\thesection.\@arabic\c@equation}
\else
\renewcommand\theequation{\@arabic\c@equation}
\fi
%******* TABLES, FIGURES
%\newcounter{figure}
\if@secfloat
 \@addtoreset{figure}{section}
 \renewcommand \thefigure {\thesection.\@arabic\c@figure}
\else
 \renewcommand \thefigure {\@arabic\c@figure}
\fi
\def\fps@figure{tbp}
\def\ftype@figure{1}
\def\ext@figure{lof}
\def\fnum@figure{\figurename~\thefigure.}
\renewenvironment{figure}
               {\let\@makecaption\@makefigurecaption \centering\@float{figure}}
               {\end@float}  
\renewenvironment{figure*}
               {\let\@makecaption\@makefigurecaption \centering\@dblfloat{figure}}
               {\end@dblfloat}
\long\def\@makefigurecaption#1#2{%
 \vskip\abovecaptionskip
\@tempdima\hsize \advance\@tempdima by-2em
\setbox\@tempboxa\hbox{\textbf{#1\kern1em}}%
\noindent\hskip2em\parbox[t]{\@tempdima}{\hangindent\wd\@tempboxa
\centering\small\textbf{#1}\hskip1em #2\par}}%\centering ?????
%
% TABLE
%\newcounter{table}
  \if@secfloat
  \@addtoreset{figure}{section}
\renewcommand \thetable{\thesection.\@arabic\c@table}
\else
  \renewcommand \thetable{\@arabic\c@table}
\fi
\def\fps@table{tbp}
\def\ftype@table{2}
\def\ext@table{lot}
\def\fnum@table{\tablename~\thetable.}
%
\renewenvironment{table}
               {\let\@makecaption\@maketablecaption%
               \let\@floatboxreset\@tableboxreset\@float{table}}
               {\end@float}
\renewenvironment{table*}
               {\let\@makecaption\@maketablecaption%
               \let\@floatboxreset\@tableboxreset\@dblfloat{table}}
               {\end@dblfloat}
%
\def\@tableboxreset{%
        \reset@font%
        \centering\small%
        \@setnobreak%
        \@setminipage%
}

%\newlength\abovecaptionskip
%\newlength\belowcaptionskip
\setlength\abovecaptionskip{2\p@}
\setlength\belowcaptionskip{6\p@}
%
\long\def\@maketablecaption#1#2{%
 \setbox\@tempboxa\hbox{\textbf{#1\kern1em}}%
 \@tempdima\hsize \advance\@tempdima by-2em%
 \hskip2em\parbox[t]{\@tempdima}{\hangindent\wd\@tempboxa\centering\small\textbf{#1\kern1em}#2\vphantom{Ay}  \par}%\centering???
 \vskip\belowcaptionskip}
%
\def\tfootnotetext{\@ifnextchar[{\@tfootnotetext}{\@tfootnotetext[\hsize]}}
\def\@tfootnotetext[#1]#2#3{%
\ifhmode\par\fi
\vspace*{1pt}
\parbox[t]{#1}{\parindent1.5pc\indent\if.#2.\else $^{#2}$\fi #3}}%
\def\tabnote{\@ifnextchar[{\@tabnote}{\@tabnote[\hsize]}}
\def\@tabnote[#1]#2{\@tfootnotetext[#1]{}{#2}}
%
%********************* COMPATIBILITY WITH OLD LATEX:
\DeclareOldFontCommand{\rm}{\normalfont\rmfamily}{\mathrm}
\DeclareOldFontCommand{\sf}{\normalfont\sffamily}{\mathsf}
\DeclareOldFontCommand{\tt}{\normalfont\ttfamily}{\mathtt}
\DeclareOldFontCommand{\bf}{\normalfont\bfseries}{\mathbf}
\DeclareOldFontCommand{\it}{\normalfont\itshape}{\mathit}
\let\sl\it
\DeclareOldFontCommand{\sc}{\normalfont\scshape}{\@nomath\sc}
%
% *********** MATH
%
%\def\tfrac#1#2{{\textstyle\frac{#1}{#2}}}
%\def\dfrac#1#2{{\displaystyle\frac{#1}{#2}}}
%
\def\dvt{\colon\ }
\def\dvtx{\nobreak\,\colon\relax}
%
\let\geq\geqslant
\let\leq\leqslant
%
\if@secthm
 \@addtoreset{thm}{section}
 \def\thethm{\thesection.\arabic{thm}}
\else
 \def\thethm{\arabic{thm}}
\fi
%
%******* BIBLIOGRAPHY
\bibliographystyle{unsrt}%??????????
\def\authors#1{#1}
\renewcommand\newblock{\hskip .11em\@plus.33em\@minus.07em}%\hskip .11em
\newdimen\bibindent
\setlength\bibindent{0pt} %{10pt}
\let\@openbib@code\@empty

\def\citationstyle#1{\csname cs@#1\endcsname}
\let\citationstyle

% DEFINITIONS FOR `NAMEYEAR' CITATION STYLE
\def\nam@thebib#1{%
      \bigskip
      \centering\textbf{\bibname}\par %
      \medskip
      \list{}%
           {\footnotesize\labelwidth\z@%
            \leftmargin\bibindent
            \itemindent-\leftmargin\vskip
            \partopsep\z@ \topsep\z@ \parsep\z@ \itemsep\z@
            \@openbib@code %???// \vskip
            }%
      \sloppy
      \clubpenalty4000
      \@clubpenalty \clubpenalty
      \widowpenalty4000%
      \sfcode`\.\@m}

\def\nam@bibitem#1{\item\if@filesw \immediate\write\@auxout
 {\string\bibcite{#1}{?}}\fi\ignorespaces}

% \@@cite is original definition of \cite
\let\@@cite=\cite
\def\citefull{\def\nameyear##1##2{##1, ##2}\@@cite}
\def\citeyear{\def\nameyear##1##2{##2}\@@cite}

% \@citex loops over the list of citation keys
\def\nam@citex[#1]#2{\if@filesw
 \immediate\write\@auxout{\string\citation{#2}}\fi
 \def\@citea{}\@cite{\@for\@citeb:=#2\do
 {\@citea\def\@citea{,\penalty\@m\ }\@ifundefined{b@\@citeb}{{\bf ?}\@warning
 {Citation `\@citeb' on page \thepage \space undefined}\special{mt:badrefs}}%
{\csname b@\@citeb\endcsname}}}{#1}}

% \@cite produces the output of \cite
\def\nam@cite#1#2{(#1\if@tempswa ; #2\fi)}


% DEFINITIONS FOR `NUMBER' CITATION STYLE

\def\num@thebib#1{%
      \bigskip
      \centering\textbf{\bibname}\par
      \medskip
      \list{\@biblabel{\@arabic\c@enumiv}}%
           {\small\settowidth\labelwidth{\@biblabel{#1}}
            \leftmargin\labelwidth
            \advance\leftmargin\labelsep
            \partopsep\z@ \topsep\z@ \parsep\z@ \itemsep\z@
            \@openbib@code
            \usecounter{enumiv}%
            \let\p@enumiv\@empty
            \renewcommand\theenumiv{\@arabic\c@enumiv}}%
      \sloppy
      \clubpenalty4000
      \@clubpenalty \clubpenalty
      \widowpenalty4000%
      \sfcode`\.\@m}

\def\num@bibitem#1{\item\if@filesw \immediate\write\@auxout
       {\string\bibcite{#1}{\the\value{\@listctr}}}\fi\ignorespaces}
\def\num@biblabel#1{[#1]}%%%%.[refer]

\newcount\@tempcntc
% \@citex loops over the list of citation keys and collapses
% citation numbers to ranges. Non-numeric and undefined labels are handled.
% The citation keys are not sorted.
\def\num@citex[#1]#2{\if@filesw\immediate\write\@auxout{\string\citation{#2}}\fi
 \@tempcnta\z@\@tempcntb\m@ne\def\@citea{}\@cite{\@for\@citeb:=#2\do
 {\@ifundefined
 {b@\@citeb}{\@citeo\@tempcntb\m@ne\@citea
 \def\@citea{,\penalty\@m\ }{\bf ?}\@warning
 {Citation `\@citeb' on page \thepage \space undefined}\special{mt:badrefs}}%
% IF \b@KEY expands to number
% \@tempcntc := expansion of \b@KEY
% ELSE
% \@tempcntc := 0; \box0 := expansion of \b@KEY
 {\setbox\z@\hbox{\global\@tempcntc0\csname b@\@citeb\endcsname\relax}%
 \ifnum\@tempcntc=\z@ \@citeo\@tempcntb\m@ne
 \@citea\def\@citea{,\penalty\@m\ }
 \hbox{\csname b@\@citeb\endcsname}%
 \else
 \advance\@tempcntb\@ne
 \ifnum\@tempcntb=\@tempcntc
 \else\advance\@tempcntb\m@ne\@citeo
 \@tempcnta\@tempcntc\@tempcntb\@tempcntc\fi\fi}}\@citeo}{#1}}

\def\@citeo{\ifnum\@tempcnta>\@tempcntb\else\@citea
 \def\@citea{,\penalty\@m\ }%
 \ifnum\@tempcnta=\@tempcntb\the\@tempcnta\else
 {\advance\@tempcnta\@ne\ifnum\@tempcnta=\@tempcntb \else \def\@citea{--}\fi
 \advance\@tempcnta\m@ne\the\@tempcnta\@citea\the\@tempcntb}\fi\fi}

% \@cite produces the output of \cite
\def\num@cite#1#2{[{#1\if@tempswa , #2\fi}]}

% \citenum emits the plain citation label without ornament
\def\citenum#1{\begingroup \def\@cite##1##2{##1}\cite{#1}\endgroup}

% DEFINITIONS FOR SELECTING `NAMEYEAR' AND `NUMBER' CITATION STYLE
\def\cs@nameyear{\let\thebibliography=\nam@thebib
\let\@biblabel=\@gobble \let\@bibitem=\nam@bibitem
% \cite is redefined to allow a *-form;
\def\cite{\@ifstar{\citeyear}{\citefull}}\let\@citex=\nam@citex
\let\@cite=\nam@cite\message{NAMEYEAR citation style}}

\def\cs@number{\let\thebibliography=\num@thebib \let\cite=\@@cite
\let\@biblabel=\num@biblabel \let\@bibitem=\num@bibitem
\let\nameyear=\@gobbletwo \let\@citex=\num@citex
\let\@cite=\num@cite\message{NUMBER citation style}}

\if@nameyear \cs@nameyear \else \cs@number \fi
%
%****************************** FRONTMATTER *
%
\newtoks\t@glob@notes
\newtoks\t@loc@notes
\newcount\note@cnt
\newcounter{author}
\newcount\n@author
\def\n@author@{}
\newcounter{address}
%
\newdimen\sv@mathsurround
\newcount\sv@hyphenpenalty
%
\newcount\prev@elem \prev@elem=0
\newcount\cur@elem  \cur@elem=0
\chardef\e@pretitle=1
\chardef\e@title=1
\chardef\e@subtitle=1
\chardef\e@author=2
\chardef\e@address=3
%
\newif\if@newelem
\newif\if@pretitle
\newif\if@firstauthor
\newif\if@preface
\newif\if@hasabstract
\newif\if@haskeywords
\newif\if@history
%
\newbox\fm@box
\newdimen\fm@size
\newbox\t@abstract
\newbox\t@keywords
%
\def\add@tok#1#2{\global#1\expandafter{\the#1#2}}
\def\add@xtok#1#2{\begingroup
  \no@harm
  \xdef\@act{\global\noexpand#1{\the#1#2}}\@act
\endgroup}
%
\def\tailthanksref[#1]#2{\noexpand\pthanksref{#1}}
\def\pthanksref#1{\global\advance\note@cnt\@ne\ifnum\note@cnt>\@ne
\global\t@loc@notes\expandafter{\the\t@loc@notes\note@sep}\fi
\global\t@loc@notes\expandafter{\the\t@loc@notes#1}}
%
\def\beg@elem{\global\t@loc@notes={}\global\note@cnt\z@}
\def\@xnamedef#1{\expandafter\xdef\csname #1\endcsname}
\def\no@harm{%
  \let\\=\relax  \let\rm\relax
  \let\ss=\relax \let\ae=\relax \let\oe=\relax
  \let\AE=\relax \let\OE=\relax
  \let\o=\relax  \let\O=\relax
  \let\i=\relax  \let\j=\relax
  \let\aa=\relax \let\AA=\relax
  \let\l=\relax  \let\L=\relax
  \let\d=\relax  \let\b=\relax \let\c=\relax
  \let\bar=\relax
  \def\protect{\noexpand\protect\noexpand}}
%
\def\proc@elem#1#2{\begingroup
    \no@harm
    \def\thanks##1##{\@gobble}%
    \def\thanksref##1##{\@gobble}%
    \@xnamedef{@#1}{#2}%
  \endgroup
  \prev@elem=\cur@elem
  \cur@elem=\csname e@#1\endcsname
  \expandafter\elem@nothanksref#2\thanksref\relax%
  \expandafter\elem@nothanks#2\thanks\relax}
%
\def\elem@nothanksref#1\thanksref{\futurelet\@peektok\elem@thanksref}
\def\elem@thanksref{\ifx\@peektok\relax
  \else \expandafter\elem@morethanksref \fi}
\def\elem@morethanksref[#1]#2{\add@thanks{#1}\elem@nothanksref}
%
\def\elem@nothanks#1\thanks{\futurelet\@peektok\elem@thanks}
\def\elem@thanks{\ifx\@peektok\relax
  \else \ifx\@peektok[ \expandafter\expandafter\expandafter\elem@morethankse
  \else \expandafter\expandafter\expandafter\elem@morethanks \fi\fi}
%
\def\elem@morethankse[#1]#2{\thanks@optarg[#1]{#2}\add@thanks{#1}\elem@nothanks}
\def\elem@morethanks#1{\thanks@optarg[]{#1}\add@thanks{}\elem@nothanks}
%
\def\add@thanks#1{%
  \global\advance\note@cnt\@ne
    \ifnum\note@cnt>\@ne \add@xtok\t@loc@notes{\note@sep}\fi
    \ifx.#1.\add@xtok\t@loc@notes{\thefootnote}\else
        \add@xtok\t@loc@notes{#1}\fi%
}
\def\add@addressref#1{%
  \global\advance\note@cnt\@ne
    \ifnum\note@cnt>\@ne \add@xtok\t@loc@notes{\note@sep}\fi
    \add@tok\t@loc@notes{\ref{#1}}%
}
\def\note@sep{,}
%
\def\thanks@optarg[#1]#2{%
    \ifx.#1.\add@tok\t@glob@notes{\footnotetext}%
    \else\add@tok\t@glob@notes{\freefootnotetext}\fi%
    \refstepcounter{footnote}%
    \ifx.#1.\add@xtok\t@glob@notes{[\the\c@footnote]}%
    \else\add@xtok\t@glob@notes{[#1]}\fi%
    \add@tok\t@glob@notes{{#2}}%
        \ignorespaces}%
%
% FRONTMATTER
%
\def\artty#1{\gdef\@artty{#1}}
\gdef\@artty{RA} % Default Research Article
\gdef\@RA{RA}%     Research Article
\gdef\@RV{RV}%     Review Article
\gdef\@XX{XX}%     Miscelaneous Article
\gdef\@AI{AI}%     Author Index
%
\newdimen\a@title@skip \a@title@skip=12pt
\newskip\b@section@skip \b@section@skip=24pt plus6pt minus6pt%
%
\def\make@AI{%
\global\a@title@skip=16pt
\gdef\@copyright{}
}
\def\frontmatter{%
  \ifx\@artty\@AI \make@AI\fi
  \let\@corresp@note\relax
  \global\t@glob@notes={}\global\c@author\z@
  \global\c@address\z@
  \sv@mathsurround\mathsurround \m@th
  \global\n@author=0\n@author@\relax
  \global\advance\n@author\m@ne
  \global\@firstauthortrue
  \global\@hasabstractfalse
  \global\@prefacefalse
  \open@fm \ignorespaces}
%
\def\preface{\@prefacetrue}
%
% ENDFRONTMATTER
%
\def\endfrontmatter{%
  \global\n@author=\c@author \@writecount
  \global\@topnum\z@
  \ifx\@firstpage\@lastpage
    \gdef\@pagerange{\@firstpage}
  \else
    \gdef\@pagerange{\@firstpage--\@lastpage}
  \fi
  \thispagestyle{copyright}%
%  \if@preface \else  \history@fmt\fi
  \newcount\c@sv@footnote
  \global\c@sv@footnote=\c@footnote
  \if@twocolumn\else
    \output@glob@notes
  \fi
  \if@preface
    \@hasabstractfalse
  \fi
  \if@hasabstract
    \normal@text
    \vskip 18pt
    \unvbox\t@abstract
    \vskip 6pt
    \unvbox\t@keywords
  \fi
  \vskip\b@section@skip%
  \close@fm
  \if@twocolumn
     \output@glob@notes
  \fi
  \global\@prefacefalse
  \global\leftskip\z@
  \global\@rightskip\z@
  \global\rightskip\@rightskip
  \global\c@footnote=\c@sv@footnote
  \global\mathsurround\sv@mathsurround
  \let\title\relax       \let\author\relax
  \let\address\relax
  \let\frontmatter\relax \let\endfrontmatter\relax
  \let\@maketitle\relax  \let\@@maketitle\relax
  \normal@text}
%
\let\maketitle\relax
%
\newdimen\t@xtheight
\def\init@settings{
\splittopskip=\topskip \splitmaxdepth=\maxdepth
\t@xtheight\textheight \advance\t@xtheight-\splittopskip}
%
\def\open@fm{
  \global\setbox\fm@box=\vbox\bgroup
  \hsize=\textwidth
  \sv@hyphenpenalty\hyphenpenalty
  \hyphenpenalty\@M}
%
\def\close@fm{\par \egroup
  \fm@size=\dp\fm@box \advance\fm@size by \ht\fm@box
  \@whiledim\fm@size>\t@xtheight \do{%
    \global\setbox\@tempboxa=\vsplit\fm@box to \t@xtheight
    \unvbox\@tempboxa %\newpage
    \fm@size=\dp\fm@box \advance\fm@size by \ht\fm@box}
  \if@twocolumn
    \emergencystretch=1pc \twocolumn[\unvbox\fm@box]
  \else
    \unvbox\fm@box
  \fi}
%
\def\output@glob@notes{\bgroup
  \the\t@glob@notes
  \egroup}
%
\def\normal@text{\global\let\\=\@normalcr
  \global\leftskip\z@ \global\@rightskip\z@ \global\rightskip\@rightskip
  \global\parfillskip\@flushglue}
%
\def\@writecount{\write\@mainaux{\string\global
  \string\@namedef{n@author@}{\the\n@author}}
}
%
% TITLE
\def\pretitle#1{\gdef\@pretitle{#1}\global\@pretitletrue}
%
\def\title#1{%
  \beg@elem
  \title@note@fmt
  \add@tok\t@glob@notes
    {\title@note@fmt}%
  \proc@elem{title}{#1}%
  \def\title@notes{\the\t@loc@notes}%
  \title@fmt{\@title}{\title@notes}%
  \ignorespaces}
%
\newdimen\@@topskip \@@topskip=4pt
%
\def\title@fmt#1#2{%
  \vspace*{\@@topskip}
  {\if@pretitle\@pretitle\par\vskip12pt\fi}
  {\centering\title@size #1\,\hbox{$^{#2}$}\par}%
  \vskip\a@title@skip%
  }
%
\def\subtitle#1{%
  \beg@elem
  \proc@elem{subtitle}{#1}%
  \def\title@notes{\the\t@loc@notes}%
  \subtitle@fmt{\@subtitle}{\title@notes}%
  \ignorespaces}
%
%
\def\subtitle@fmt#1#2{%
  {\subtitle@size #1\,\hbox{$^{\mathrm{#2}}$}\par}%
  \vskip\a@title@skip%
  }
%
\def\title@note@fmt{\def\thefootnote{\sxarabic{footnote}}}
%
% AUTHOR
%
\newdimen\b@author@skip
\b@author@skip 12pt 
%
\def\author{\@ifnextchar[{\author@optarg}{\author@optarg[]}}
%
\def\author@optarg[#1]#2{\stepcounter{author}%???????
  \beg@elem\def\degs##1{##1}\def\fnms##1{##1}\def\inits##1{##1}%
        \def\snm##1{##1}\def\roles##1{##1}%
  \if@firstauthor%
  \first@author \global\@firstauthorfalse \fi%
  \@for\@tempa:=#1\do{\expandafter\add@addressref\expandafter{\@tempa}}%
  \proc@elem{author}{#2}%
  \author@fmt{\the\c@author}{\the\t@loc@notes}{\@author}}%
%
\newbox\author@box
%
\def\author@fmt#1#2#3{\@newelemtrue
  \ifnum\prev@elem=\e@author \global\@newelemfalse \fi
  \if@newelem \author@fmt@init \fi
  \edef\@tempb{#2}\ifx\@tempb\@empty
    \hbox{#3}\else
    \hbox{#3\,$^{\mathrm{#2}}$}
  \fi}
%
\def\first@author{\author@note@fmt%
  \add@tok\t@glob@notes%
    {\author@note@fmt}}%
%
\def\author@fmt@init{%
  \par
  \vskip \b@author@skip
  \authors@size\centering
  \leavevmode}
%
\def\and{\unskip~and~}
%
\def\author@note@fmt{%
  \def\thefootnote{\sxarabic{footnote}}}
%
\def\sxarabic#1{%
        \expandafter\ifcase\value{#1} \or *\or **\or *** \or **** \or *****\fi
}
%
% ADDRESS
%
\def\email#1{{{\Lat \itshape e-mail}:\ {\Lat #1 }}}%up
%
\def\address{\@ifstar{\address@star}%
  {\@ifnextchar[{\address@optarg}{\address@noptarg}}}
%
\def\address@optarg[#1]#2{\refstepcounter{address}%
  \beg@elem
  \proc@elem{address}{#2}%
  \address@fmt{\the\c@address}{\the\t@loc@notes}{\@address}\label{#1}%
  \ignorespaces}
%
\def\address@noptarg#1{\refstepcounter{address}%
  \beg@elem
  \proc@elem{address}{#1}%
  \address@fmt{\z@}{\the\t@loc@notes}{\@address}%
  \ignorespaces}
%
\def\address@star#1{%
  \beg@elem
  \proc@elem{address}{#1}%
  \address@fmt{\m@ne}{\the\t@loc@notes}{\@address}%
  \ignorespaces}
%
\def\theaddress{\arabic{address}}%
%
\def\address@fmt#1#2#3{\@newelemtrue
  \ifnum\prev@elem=\e@address \@newelemfalse \fi
  \if@newelem \address@fmt@init \fi
  \centering\bgroup\parskip\z@\noindent\footnotesize\itshape %
  \ifnum#1=\z@
    #3\,$^{\mathrm{#2}}$\space%
  \else
    \ifnum#1=\m@ne
      $^{\phantom{\mathit{\theaddress}}\,}$#3\,$^{\mathrm{#2}}$%
    \else
      $^{\mathit{\theaddress}\,}$#3\,$^{\mathrm{#2}}$%
    \fi
  \fi
  \par\egroup}
%
\def\address@fmt@init{%
        \def\@currentlabel{\theaddress}
  \par
  \vskip 4pt plus 1pt minus 1pt}
%
% ABSTRACT
%
\def\abstract{\@ifnextchar[{\@abstract}{\@abstract[]}}
\def\@abstract[#1]{%
  \global\@hasabstracttrue
  \hyphenpenalty\sv@hyphenpenalty
  \global\setbox\t@abstract=\vbox\bgroup\linewidth\textwidth
% \advance\linewidth by-6pc 
  \@totalleftmargin\z@\leftskip\z@
  \@rightskip\z@ \rightskip\@rightskip
  \parfillskip\@flushglue
  \small\baselineskip 13pt
  \parindent 1.5pc
  {\bfseries\abstractname\ }
  \ignorespaces}
\def\endabstract{\par\egroup}%
% KEYWORDS
\def\sep{\unskip, }
\global\@haskeywordsfalse
\newdimen\dp@t@keywords
\def\keyword{\global\@haskeywordstrue\global\setbox\t@keywords=\vbox\bgroup%
  \normal@text\parindent 1.5pc\small\baselineskip13pt\textbf{\keywordsname:\ }\ignorespaces}
\def\endkeyword{\par\egroup\global\dp@t@keywords=\dp\t@keywords}
\def\keywords#1{\begin{keyword}#1\end{keyword}}
%
% JORNAL, VOLUME, ISSUE
%
\def\journal#1{\gdef\@journal{#1}}    \@ifundefined{@journal}{\gdef\@journal{Journal not defined}}{}
\def\volume#1{\gdef\@volume{#1}}      \def\@volume{0}
\def\issue#1{\gdef\@issue{#1}}        \def\@issue{0}
%
%
\newcount\@pubyear
\newcount\@copyear
\@pubyear=\number\year
\@copyear\@pubyear \advance\@copyear-1900
\def\pubyear#1{\global\@pubyear#1
  \global\@copyear\@pubyear \global\advance\@copyear-1900
  \ignorespaces}
%

\def\firstpage#1{\def\@tempa{#1}\ifx\@tempa\@empty\else
  \gdef\@firstpage{#1}\gdef\@lastpage{#1}%
  \global\c@page=#1 \ignorespaces\fi
  }
\def\@firstpage{1}
\def\lastpage#1{\def\@tempa{#1}\ifx\@tempa\@empty\else
  \gdef\@lastpage{#1}\ignorespaces\fi}
\def\@lastpage{0}
\def\@pagerange{1--0}
% SGML
\long\def\convertas#1#2{#2}
\def\sday#1{#1}\def\smonth#1{#1}\def\syear#1{#1}
\def\aid#1{\gdef\@aid{#1}}
%
\def\SSDI#1{\gdef\@ssdi{#1}} \def\@ssdi{010003-25}
\def\issn#1{\gdef\@issn{#1}} \def\@issn{1058-9244}
\def\price#1{\gdef\@price{#1}} \def\@price{8}
%
\def\date#1{\gdef\@date{#1}}    \def\@date{\today}
%
% Received, accepted etc.
%
\def\received#1{\def\@tempa{#1}\ifx\@tempa\@empty\else\gdef\@received{#1}\global\@historytrue\fi}
  \def\@received{\@nil}
\def\revised#1{\def\@tempa{#1}\ifx\@tempa\@empty\else\gdef\@revised{#1}\fi}
  \def\@revised{\@nil}
\def\accepted#1{\def\@tempa{#1}\ifx\@tempa\@empty\else\gdef\@accepted{#1}\fi}
  \def\@accepted{\@nil}
\def\articletype#1{\gdef\@articletype{#1}}
  \@ifundefined{@articletype}{\def\@articletype{}}{}
%
\def\received@prefix{{\cyr Prim\lj{}eno}~}
\def\revised@prefix{;~{\cyr Ispravljeno}~}
\def\accepted@prefix{;~{\cyr Prihva\cc{}eno}~}
%
\def\empty@data{\@nil}
%
\def\history@fmt{%
  \bgroup\small
  \vskip\b@history@skip
  \ifx\@received\empty@data \else
    \leavevmode
    \history@prefix
    \received@prefix\@received \received@postfix%
    \ifx\@revised\empty@data \else
      \revised@prefix\@revised \revised@postfix%
    \fi
    \ifx\@accepted\empty@data \else
      \accepted@prefix\@accepted \accepted@postfix%
    \fi
    \history@postfix
  \fi
  \par \egroup}
%***************** BACKMATTER
\newcommand\backmatter{\vfill\normalsize\thereceived\eject}
\def\thereceived{{\ifx\@received\empty@data \else
    \leavevmode\raggedleft\received@prefix\@received\par\fi}}%raggedleft
\newenvironment{biography}{\def\author##1{\textbf{##1}}\goodbreak}{\vspace{12pt}}

\newenvironment{abstractLT}{\bgroup\small%%%
\def\title##1{{\normalsize\raggedright\textbf{##1}\par\smallskip}}%centering
\def\authors##1{{\normalsize\raggedright##1\par\smallskip}}%centering%%%%%
}{\par\egroup}
%**************** INICIALIZATION
%
% Define font psyr for copyright:
\DeclareFixedFont{\copyrf}{U}{psy}{m}{n}{8}
\DeclareFixedFont{\copyrfa}{U}{psy}{m}{n}{9}
\def\copyright@sign{{\copyrf\char'323}}
\def\copyright@signa{{\copyrfa\char'323}}
%
% DIMENSIONS
\def\@articletypesize{\large}
\def\pretitle@size{\large\bfseries}
\def\title@size{\large\bfseries}
\def\subtitle@size{\large}
\def\authors@size{\normalsize}
\def\address@size{\small\itshape}
% Block preparation of contents:
%\def\addcontentsline#1#2#3{}
%\long\def\addtocontents#1#2{}
%
\renewcommand\today{}
\edef\today{\ifcase\month\or
  January\or February\or March\or April\or May\or June\or
  July\or August\or September\or October\or November\or December\fi
  \space\number\day, \number\year}
%
\@twosidetrue
\pagestyle{headings}
\pagenumbering{arabic}
\frenchspacing
\init@settings
\endinput
%%
%% End of file mpaconference.cls'.
