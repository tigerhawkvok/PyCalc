import math,re,warnings #,traceback

# Implicit multiplication
# Math in functions - 90%
# Fix splitting for adv - ~ln242
# Manual for plot types and line styles on plot

warnings.filterwarnings(action='ignore')

lastNum=0
radians=True
sigfig=12

binary = {
        '+':lambda a,b:a+b,
        '-':lambda a,b:a-b,
        '/':lambda a,b:a/b,
        '*':lambda a,b:a*b,
        '^':lambda a,b:math.pow(a,b),
        '%':lambda a,b:a%b,
        }

result = {
        'sin':lambda x:math.sin(trigMode(x)),
        'cos':lambda x:math.cos(trigMode(x)),
        'tan':lambda x:math.tan(trigMode(x)),
        'cot':lambda x:1/math.tan(trigMode(x)),
        'csc':lambda x:1/math.sin(trigMode(x)),
        'sec':lambda x:1/math.cos(trigMode(x)),
        'sinh':lambda x:sinh(trigMode(x)),
        'cosh':lambda x:cosh(trigMode(x)),
        'tanh':lambda x:tanh(trigMode(x)),
        'sech':lambda x:1/cosh(trigMode(x)),
        'csch':lambda x:1/sinh(trigMode(x)),
        'coth':lambda x:1/tanh(trigMode(x)),
        'asin':lambda x:math.asin(trigMode(x)),
        'acos':lambda x:math.acos(trigMode(x)),
        'atan':lambda x:math.atan(trigMode(x)),
        'acot':lambda x:math.atan(trigMode(1/x)),
        'acsc':lambda x:math.asin(trigMode(1/x)),
        'asec':lambda x:math.acos(trigMode(1/x)),
        'asinh':lambda x:asinh(trigMode(x)),
        'acosh':lambda x:acosh(trigMode(x)),
        'atanh':lambda x:atanh(trigMode(x)),
        'acsch':lambda x:acsch(trigMode(x)),
        'asech':lambda x:asech(trigMode(x)),
        'acoth':lambda x:acoth(trigMode(x)),
        'sqrt':lambda x:math.sqrt(x),
        'ln':lambda x:math.log(x),
        'log':lambda x,a:math.log(x,a),
        'log10':lambda x:math.log10(x),
        'pow':lambda x,a:math.pow(x,a),
        'mod':lambda x,a:x%a,
        'rem':lambda x,a:x%a,
        'root':lambda x,a:math.pow(x,1/a),
        'exp':lambda x:math.exp(x),
        'set_sigfig':lambda x:set_sigs(x),
        'set_radians':lambda x:radianMode(x),
        'set_degrees':lambda x:degreeMode(x),
        #'base2':lambda x:toBase2(x),
        #'tobase2':lambda x:toBase2(x),
        #'binary':lambda x:toBase2(x),
        #'dec':lambda x:toBase10(x),
        #'base10':lambda x:toBase10(x),
        #'tobase10':lambda x:toBase10(x),
        #factorial 
        #comb, perm 
        #gamma,zeta 
        #Bessel? 
        #stat stuff - stddev, mean, variance, 
        #graphability 
        }
multiarg = {
        'log':math.exp(1),
        'pow':2,
        'root':2,
        'rem':1,
        'mod':1,
        'lsfit':1,
        'plot':1,
        'graph':1
        }
numbers = {
    'pi':math.pi,
    'e':math.exp(1),
    'c':299792458, #defined, universal
    'h':6.62606896*math.pow(10,-34), #universal, 2006 CODATA
    'G':6.67428*math.pow(10,-11), #universal, 2006 CODATA
    'mu0':4*math.pi*math.pow(10,-7), #defined
    'q0':1.602176487*math.pow(10,-19),#2006 CODATA
    'nA':6.0221415*math.pow(10,23),#2006 CODATA
    'me':9.10938188*math.pow(10,-31),#2006 CODATA
    'mp':1.67262158*math.pow(10,-27),#2006 CODATA
    'mn':1.67492729*math.pow(10,-27),#2006 CODATA
    'R':8.314472, #2006 CODATA
    }
## Recursed numbers - defined in terms of above. When above change, then these will auto-update
numbers['hbar']=numbers['h']/(2*math.pi)
numbers['e0']=1/(4*math.pi*math.pow(10,-7)*math.pow(numbers['c'],2))
numbers['kb']=numbers['R']/numbers['nA']
numbers['sigma']=math.pow(math.pi,2)*math.pow(numbers['kb'],4)/(60*math.pow(numbers['hbar'],3)*math.pow(numbers['c'],2))
numbers['alpha']=math.pow(numbers['q0'],2)/(4*math.pi*numbers['e0']*numbers['hbar']*numbers['c'])
# Planck values
numbers['lP']=math.sqrt(numbers['hbar']*numbers['G']/math.pow(numbers['c'],3))
numbers['mP']=math.sqrt(numbers['hbar']*numbers['c']/numbers['G'])
numbers['tP']=math.sqrt(numbers['hbar']*numbers['G']/math.pow(numbers['c'],5))
numbers['qP']=math.sqrt(4*math.pi*numbers['e0']*numbers['hbar']*numbers['c'])
numbers['TP']=math.sqrt(numbers['hbar']*math.pow(numbers['c'],5)/(numbers['G']*math.pow(numbers['kb'],2)))

manual = {
    'sin':'SYNTAX:\n\t sin(x) \nDESCRIPTION:\n\t The sine of x.',
    'cos':'SYNTAX:\n\t cos(x) \nDESCRIPTION:\n\t The cosine of x.',
    'tan':'SYNTAX:\n\t tan(x) \nDESCRIPTION:\n\t The tangent of x.',
    'cot':'SYNTAX:\n\t cot(x) \nDESCRIPTION:\n\t The cotangent of x (1/tan(x)).',
    'csc':'SYNTAX:\n\t csc(x) \nDESCRIPTION:\n\t The cosecant of x (1/sin(x)).',
    'sec':'SYNTAX:\n\t sec(x) \nDESCRIPTION:\n\t The secant of x (1/cos(x)).',
    'sinh':'SYNTAX:\n\t sinh(x) \nDESCRIPTION:\n\t The hyperbolic sin of x.',
    'cosh':'SYNTAX:\n\t cosh(x) \nDESCRIPTION:\n\t The hyperbolic cosine of x.',
    'tanh':'SYNTAX:\n\t tanh(x) \nDESCRIPTION:\n\t The hyperbolic tangent of x.',
    'sech':'SYNTAX:\n\t sech(x) \nDESCRIPTION:\n\t The hyperbolic secant of x.',
    'csch':'SYNTAX:\n\t csch(x) \nDESCRIPTION:\n\t The hyperbolic cosecant of x.',
    'coth':'SYNTAX:\n\t coth(x) \nDESCRIPTION:\n\t The hyperbolic cotangent of x.',
    'asin':'SYNTAX:\n\t asin(x) \nDESCRIPTION:\n\t The inverse of sin(x).',
    'acos':'SYNTAX:\n\t acos(x) \nDESCRIPTION:\n\t The inverse of cos(x).',
    'atan':'SYNTAX:\n\t atan(x) \nDESCRIPTION:\n\t The inverse of tan(x).',
    'acot':'SYNTAX:\n\t acot(x) \nDESCRIPTION:\n\t The inverse of cot(x).',
    'acsc':'SYNTAX:\n\t acsc(x) \nDESCRIPTION:\n\t The inverse of csc(x).',
    'asec':'SYNTAX:\n\t asec(x) \nDESCRIPTION:\n\t The inverse of sec(x).',
    'asinh':'SYNTAX:\n\t asinh(x) \nDESCRIPTION:\n\t The inverse of sinh(x).',
    'acosh':'SYNTAX:\n\t acosh(x) \nDESCRIPTION:\n\t The inverse of cosh(x). Only defined where x>=1.',
    'atanh':'SYNTAX:\n\t atanh(x) \nDESCRIPTION:\n\t The inverse of tanh(x). Only defined where x^2<1.',
    'acsch':'SYNTAX:\n\t acsch(x) \nDESCRIPTION:\n\t The inverse of csch(x). Only defined where x is not 0.',
    'asech':'SYNTAX:\n\t asech(x) \nDESCRIPTION:\n\t The inverse of sech(x). Only defined where x is between 0 and 1.',
    'acoth':'SYNTAX:\n\t acoth(x) \nDESCRIPTION:\n\t The inverse of coth(x).',
    'sqrt':'SYNTAX:\n\t sqrt(x) \nDESCRIPTION:\n\t The square root of x. This is equivalent to the function pow(x,.5).',
    'ln':'SYNTAX:\n\t ln(x) \nDESCRIPTION:\n\t The natural logarithm of x. This is equivalent to log(x).',
    'log':'SYNTAX:\n\t log(x,y) \nDESCRIPTION:\n\t The base y logarithm of x. If y is omitted, y is assumed to be e (Euler\'s number). In that case, the function is a synonym to ln(x).',
    'log10':'SYNTAX:\n\t log10(x) \nDESCRIPTION:\n\t The base 10 logarithm of x, also known as the common log.',
    'pow':'SYNTAX:\n\t pow(x,y) OR x^y \nDESCRIPTION:\n\t The yth power of x. If y is omitted, y is assumed to be 2.',
    'mod':'SYNTAX:\n\t mod(x,y) OR x%y \nDESCRIPTION:\n\t The modulus, or remainder, of x/y.',
    'rem':'SYNTAX:\n\t rem(x,y) OR x%y \nDESCRIPTION:\n\t The modulus, or remainder, of x/y.',
    'root':'SYNTAX:\n\t root(x,y) \nDESCRIPTION:\n\t The yth root of x. If y is omitted, y is assumed to be 2. In that case, the function is a synonym to sqrt(x).',
    'exp':'SYNTAX:\n\t exp(x) OR e^x \nDESCRIPTION:\n\t The xth power of Euler\'s number.',
    'set_sigfig':'SYNTAX:\n\t set_sigfig x \nDESCRIPTION:\n\t Set the number of displayed significant figures. Default: 12.',
    'set_radians':'SYNTAX:\n\t set_radians \nDESCRIPTION:\n\t Set the trigonometry mode to radians. This is the default.',
    'set_degrees':'SYNTAX:\n\t set_degrees \nDESCRIPTION:\n\t Set the trigonometry mode to degrees.',
    'tensor':'SYNTAX:\n\t [[1,2,3],[4,5,6],[7,8,9]] generates a 3x3 rank-2 tensor \nDESCRIPTION:\n\t This command is NOT a function. However, to enter a tensor of arbitrary rank, you follow the pattern described above.',
    'lsfit':'SYNTAX:\n\t lsfit(x,y,z) \nDESCRIPTION:\n\t The least squares fit for a set of points x and y, according to mode z. If z is omitted, it is assumed to be 1, or a linear fit. For all numerical values of z, a power fit is assumed. The special fits \'exp\' (exponentional), \'log\' (logarithmic), and \'trig\' (sin+cos) are also accepted.',
    'plot':'SYNTAX:\n\t  plot(x,y,title,x_axis_title,y_axis_title,mode,line_style) \nDESCRIPTION:\n\t Plots a graph. Only the first three arguments (x, y, and title) are required; the rest are all optional.\n \t x can be entered either as a list of coordinates like [1,2,3], as a single number (like 5), or as a range (like -2->4). "->" is used to indicate a range. If either a number or a range is entered, 1000 steps are automatically used. \n\t y  can be entered either as a range of coordinates (as x), or as a function using most mathematical operations. If a range or number is used for x, a function must be used for y (or you must enter 1000 corresponding points). The dependant variable in the function must be a capital X, eg, sin(X).\n\t Trigonometry is always done in radians when plotting.',
    'graph':'SYNTAX:\n\t  graph(x,y,title,x_axis_title,y_axis_title,mode,line_style) \nDESCRIPTION:\n\t See \'plot\'.',
    'hbar': 'VALUE:\n\t '+str(numbers['hbar'])+' \nABOUT:\n\t The reduced Planck\'s constant, or h/2pi. In kg m^2 s^{-1}, or J s (SI).',
    'pi': 'VALUE:\n\t '+str(numbers['pi'])+' \nABOUT:\n\t The ratio of a circle\'s circumfrence to its diameter.',
    'e': 'VALUE:\n\t '+str(numbers['e'])+' \nABOUT:\n\t Euler\'s number. The number such that d(e^x)/dx=1 where x=0, or the value of (1+1/n)^n as n->infinity',
    'c': 'VALUE:\n\t '+str(numbers['c'])+' \nABOUT:\n\t The speed of light in a vacuum in m/s (SI, defined).',
    'h': 'VALUE:\n\t '+str(numbers['h'])+' \nABOUT:\n\t Planck\'s constant, in kg m^2 s^{-1}, or J s (SI).',
    'G': 'VALUE:\n\t '+str(numbers['G'])+' \nABOUT:\n\t The universal gravitational constant, in m^3 kg^{-1} s^{-2} (SI).',
    'mu0': 'VALUE:\n\t '+str(numbers['mu0'])+' \nABOUT:\n\t The vacuum permeability, in kg m s^{-2} A^{-2}, or H m^{-1} (SI, defined).',
    'e0': 'VALUE:\n\t '+str(numbers['e0'])+' \nABOUT:\n\t The vacuum permittivity, in A^2 s^4 kg^{-1} m^{-3}, or F/m (SI).',
    'q0': 'VALUE:\n\t '+str(numbers['q0'])+' \nABOUT:\n\t The electronic charge, or the charge of an electron or proton (three times a quark charge). In C (SI).',
    'nA': 'VALUE:\n\t '+str(numbers['nA'])+' \nABOUT:\n\t Avogadro\'s number; the number of atoms in one mol of a substance.',
    'me': 'VALUE:\n\t '+str(numbers['me'])+' \nABOUT:\n\t The mass of an electron, in kg.',
    'mp': 'VALUE:\n\t '+str(numbers['mp'])+' \nABOUT:\n\t The mass of a proton, in kg.',
    'mn': 'VALUE:\n\t '+str(numbers['mn'])+' \nABOUT:\n\t The mass of a neutron, in kg.',
    'R': 'VALUE:\n\t '+str(numbers['R'])+' \nABOUT:\n\t The gas constant, in J K^{-1} mol^{-1} (SI). Equivalent to kb*nA.',
    'kb': 'VALUE:\n\t '+str(numbers['kb'])+' \nABOUT:\n\t Boltzmann\'s constant. The constant of proportionality between the pressure and volume of a collection of molecules, and the number and bulk temperature. In kg m^2 s^{-2} K^{-1}, or J K^{-1} (SI).',
    'sigma': 'VALUE:\n\t '+str(numbers['sigma'])+' \nABOUT:\n\t The Stefan-Boltmzmann constant. The constant of proportionality relating radiated energy and surface temperature. In kg s^{-3} K^{-4}, or W m^{-2} K^{-4} (SI)',
    'alpha': 'VALUE:\n\t '+str(numbers['alpha'])+' \nABOUT:\n\t The fine-structure constant. The coupling constant describing the strength of the electromagnetic interaction. This number is dimensionless.',
    'lP': 'VALUE:\n\t '+str(numbers['lP'])+' \nABOUT:\n\t One Planck length, in m.',
    'mP': 'VALUE:\n\t '+str(numbers['mP'])+' \nABOUT:\n\t One Planck mass, in kg.',
    'tP': 'VALUE:\n\t '+str(numbers['tP'])+' \nABOUT:\n\t One Planck time, in s.',
    'qP': 'VALUE:\n\t '+str(numbers['qP'])+' \nABOUT:\n\t One Planck charge, in C.',
    'TP': 'VALUE:\n\t '+str(numbers['TP'])+' \nABOUT:\n\t One Planck temperature, in K.',
    }

uservar= { }


def handler(): 
    eqn=''
    while eqn!='exit': 
        try: eqn=raw_input("> ") 
        except NameError: eqn=input("> ")
        try:val=readEquation(eqn) 
        except:
            import sys, traceback
            val=[False,"UnknownError::ParseError: Entry '"+str(eqn)+"' caused an unknown error. (Reported: '"+str(sys.exc_info()[0])+"' on line "+str(traceback.extract_tb(sys.exc_info()[2])[1][1])+")"]
            # for error in sys.exc_info():
            #     print(error)
            # print(traceback.extract_tb(sys.exc_info()[2]))
        if val[0] != False: 
            try:out=round_to_n(float(val[1]),sigfig)
            except ValueError:out=''
            except TypeError: 
                print(val[1])
                out=''
            print('>>> '+str(out))
            global lastNum
            lastNum=val[1]
        elif eqn == 'help' or eqn == '?': 
            print("List of available functions: ")
            for key,value in result.items(): print('\t'+key)
            print("\nSpecial values are")
            for key,value in numbers.items(): print('\t'+key+' > '+str(value))
            print("\nThe letter 'x' can be used to represent the last result.")
            print("\nType 'man' followed by the name of the function to get a description. Type 'exit' to exit.")
        elif eqn.find("man ")==0:
            pos=eqn.find(" ")
            func=eqn[pos+1:]
            if func in manual:
                print(manual[func])
            else: print("No manual entry found for '"+str(func)+"'")
        elif eqn=='man':
            print("Please specify what you would like to look up the manual entry of. A full list of functions can be found by typing 'help'.")
        elif val[1]=='OK': pass
        elif val[1]=='AdvOK':
            # Actually display custom output
            print("\t"+val[2])
        elif eqn=='': 
            try: raw_input("> ")
            except NameError: eqn=input("> ")
        elif eqn != 'exit': 
            print("Unrecognized input ("+str(val[1])+").")
            #Enter 'rpnmode' if you meant to be in Reverse Polish Notation mode.") 

def readEquation(string_in): 
    string_in=string_in.strip()
    fparse=''
    setvar=string_in.find("=")
    if setvar>0:
        store=string_in[:setvar]
        string_in=string_in[setvar+1:]
    else: store=False
    ops=formatInput(string_in)
    ops_temp=string_in.split("(")
    tensorTest=string_in.find("[")
    advTest=adv_math(ops_temp[0],'testfunction','force','')
    #print(advTest)
    #print('Ops: '+str(ops))
    #print(ops_temp)
    if advTest[0]:
        # advanced functions handle tensors on their own
        tensorTest=-1
        #fix splitting for mixed content, etc.
        ops_temp=resplit(ops_temp,"],",True)
        ops_temp=resplit(ops_temp,"',",True)
        #print(ops_temp)
        ops=[string_in] # leave the parsing to the functions
    i=0
    n=0
    for op in ops: 
        #print('going to look at '+str(op)+' with n='+str(n)+' from :')
        #print(ops)
        if op in numbers: op=str(numbers[op])
        if op=='x': op=lastNum
        if op in uservar: op=uservar[op]
        clean=op.replace("(","")
        clean=clean.replace(")","")
        endParen=''
        begParen=''
        if not is_numeric(clean) and n==0 and tensorTest<0:
            #print('looking at '+str(op))
            if op.endswith(")"):
                endParen=')'
                op=op[:-1]
            if op.find("(")==0:
                begParen='('
                op=op[1:]
            arg=''
            fof=''
            pos=op.find("_")
            if pos >=0:
              #Found an underscore
                try: dummy=result[op]('runtesttext') # is it set_sigfigs or set_degrees or set_radians?
                except: 
                    # proceed as normal on any exception
                    arg=op[pos+1:]
                    op=op[:pos]
                else:
                    # Only the functions that take dummy args will be OK
                    if dummy!=False: return [False,'OK']
            pos=op.find("(")
            if pos>0:
                args=op[pos+1:]
                pos3=args.find(",")
                op=op[:pos]
                endParen=''
                try: 
                    if ops[i+1].find("-")<0: pargs=True
                    else: pargs=False
                except IndexError: pargs=True
                if pos3>0:
                    if op not in multiarg:
                        return [False,"ParseError: Multiple arguments not supported for '"+str(op)+"'."]
                    fof=args[:pos3]
                    arg=args[pos3+1:]
                    test=adv_math(op,'testfunction','force','')
                    if test[0]:
                        if not test[1]:
                            retest=adv_math(op,'testfunction','','')
                            return retest
                        pos4=arg.find(",")
                        arg1=fof
                        arg15=arg[pos4+1:]
                        pos5=arg15.find(",")
                        arg2=arg[:pos4]#arg15[:pos5]
                        arg3=arg15#[pos5+1:]
                        #print(arg1)
                        #print(arg2)
                        #print(arg3)
                        #print(arg)
                        #print(arg15)
                    elif not test[0]: 
                        #if test[1]==False: return test
                        pos4=arg.find(",")
                        # other more args stuff
                else: 
                    fof=args
                    test=[False,'Skip']
                try:
                    #print('Entering try')
                    #print(ops[i])
                    #print(ops[i+1])
                    #print(ops[i+2])
                    if ops[i+1] in binary and not test[0]:
                        #print('Found binary op')
                        # parse the equation
                        m=0
                        innereq=fof+' '
                        foundinner=False
                        for op2 in ops:
                            if m > i and not foundinner:
                                if op2.find(")")>=0: 
                                    foundinner=True
                                    op2=op2.replace(")","")
                                innereq+=op2+' '
                                ops[m]=''
                                if op2.find("(")>=0: return [False,"ParseError: Parenthesis within functions are not supported."]
                            m+=1
                        #print('Constructed equation: '+str(innereq))
                        if innereq.find(",")>=0: return [False,"ParseError: Functions not supported in functions when using multiple arguments."]
                        innereq_p=parseBinary(innereq)
                        #print(innereq_p)
                        if is_numeric(innereq_p): fof=innereq_p
                        else: return innereq_p
                        #print(ops)
                        #print(op)
                except IndexError: pass
            else: 
                test=[False,'Skip']
                pargs=False
            m=re.search('[0-9]+',op)
            try: mg=m.group(0)
            except AttributeError: mg='false'
            if is_numeric(mg):
                arg=m.group(0)
                n=re.search('[a-zA-Z]+',op)
                try:op=n.group(0)
                except AttributeError: pass; #leave op as op
            # op and arguments should be seperated now
            #does op exist?
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                global result
                #print('Looking at '+op)
            if op in result:
                #now we can fill in secondary arguments if needed
                needarg=False
                if arg=='':
                    if op in multiarg: 
                        arg=multiarg[op]
                        needarg=True
                else: needarg=True
                # Read ahead
                if fof=='': 
                    try:fof=ops[i+1]
                    except IndexError: 
                        if op not in multiarg and arg!='': 
                            fof=arg
                            needarg=False
                        else:
                            if arg!='': extra=". Did you mean '"+str(arg)+"' to be the argument?"
                            else: extra=''
                            return [False,"BadArgument: (function: '"+op+"')"+extra]
                if fof=='x': fof=lastNum
                fofo=parseBinary(fof)
                #print(fofo)
                #print(fof)
                if not fofo[0]:
                    #print(fof)
                    nn=re.search('[a-zA-Z0-9]+',ops[i+2])
                    try: nextarg=nn.group(0)
                    except AttributeError:pass #Should be handled elsewhere
                    else:
                        #print('Found:'+str(nextarg))
                        if nextarg in numbers: nextarg=numbers[nextarg]
                        if fof=='-' and is_numeric(nextarg):
                            fof=str(fof)+str(nextarg)
                            #print('NextArg:')
                            #print(fof)
                            fofo=[True,fof]
                            #ops[i+2]='' #this should only trigger for neg numbers
                try:
                    fof=float(fof)
                    #print(fof)
                    found=False
                    if string_in.find(")")>=0:
                        substring=string_in.split("(")
                        substring=resplit(substring,")")
                        for sub in substring:
                            if type(fofo) is list: fofo=fofo[1]
                            negApp=False
                            if sub[0:1]=='-':
                                sub=sub[1:]
                                negApp=True
                            if sub in numbers: sub=str(numbers[sub])
                            if negApp: sub='-'+sub
                            pos=sub.find(str(fofo))
                            if pos>=0 and not found:
                                pos3=sub.find(",")
                                if pos3>0:
                                    sub=sub[:pos3]
                                #print(sub)
                                found=True
                                if not is_numeric(sub): fof=readEquation(sub)
                                else: fof=fofo
                                if is_numeric(fof): check=True
                                else: check=fof[0]
                                if check: 
                                    if is_numeric(fof): check=fof
                                    else: check=fof[1]
                                    try:fof=float(check)
                                    except ValueError: 
                                        return [False,'BadValue: '+str(op)+' on '+str(fof)]
                                    except IndexError: 
                                        if is_numeric(fof): fof=float(fof)
                                        else: return [False,'BadValue: '+str(op)+' on '+str(fof)]
                                    else: fof=check
                                    m=0
                                    found2=False
                                    for op2 in ops:
                                        if m > i and not found2 and not pargs: 
                                            ops[m]=''
                                            if op2.find(")")>=0: found2=True
                                        m+=1
                                else: 
                                    if type(fof) is list and not fof[0]:return fof
                                    else: return [False,"UnknownError::parseFunctionArgument: "+str(fof)]
                except ValueError: 
                    found=False
                    if string_in.find(")")>=0:
                        substring=string_in.split("(")
                        substring=resplit(substring,")")
                        #print(substring)
                        for sub in substring:
                            #if type(fofo) is list: 
                            #    if fofo[0]: fofo=fofo[1]
                            #    else: return fofo
                            if type(fofo) is list: fofo=fofo[1]
                            negApp=False
                            if sub[0:1]=='-':
                                sub=sub[1:]
                                negApp=True
                            if sub in numbers: sub=str(numbers[sub])
                            if negApp: sub='-'+sub
                            pos=sub.find(str(fofo))
                            try:pos=sub.find(fofo)
                            except TypeError: return  [False,"BadArgument: '"+str(fofo)+"' for function '"+op+"'"]
                            if pos>=0 and not found:
                                found=True
                                if not is_numeric(sub): fof=readEquation(sub)
                                else: fof=fofo
                                if is_numeric(fof): check=True
                                else: check=fof[0]
                                if check: 
                                    if is_numeric(fof): check=fof
                                    else: check=fof[1]
                                    try:fof=float(check)
                                    except ValueError: return [False,"BadArgument: '"+str(fof)+"' for function '"+op+"'"]
                                    m=0
                                    found2=False
                                    for op2 in ops:
                                        if m > i and not found2 and not pargs: 
                                            ops[m]=''
                                            if op2.find(")")>=0: found2=True
                                        m+=1
                                else: 
                                    if type(fof) is list and not fof[0]:return fof
                                    else: return [False,"UnknownError::parseFunctionArgument: "+str(fof)]
                #print('Been passed '+str(fof)+' for op '+op)
                if not is_numeric(fof):
                    # one last shot at redemption
                    o=re.search('[a-zA-z]+',fof)
                    try: res=o.group(0)
                    except AttributeError: return [False,"BadArgument: '"+str(fof)+"' for function '"+op+"'"]
                    if res in result:
                        fofo=fof
                        fof=readEquation(fof)
                        try: fof=float(fof[1])
                        except TypeError: return [False,'BadArgument: '+str(fofo)+" for function '"+op+"'"]
                    elif res in numbers: fof=numbers[res]
                    else: return [False,"BadArgument: '"+str(fof)+"' for function '"+op+"'"]
                if not pargs:n=1
                try:fof=float(fof)
                except TypeError: return [False,"BadArgument: '"+str(fof)+"' for function '"+op+"'"]
                if needarg: 
                    try: arg=float(parseBinary(arg))
                    except ValueError: 
                        return [False,'BadOptionalArgument: '+str(op)+' on '+str(fof)+' with argument '+str(arg)+' - arguments can have binary operations, but no functions']
                    else: 
                        try:fparse+=begParen+str(result[op](fof,arg))+endParen+' '
                        except TypeError: return [False,"BadArgument: '"+str(fofo)+"' for function '"+op+"'"]
                else: 
                    try:fparse+=begParen+str(result[op](fof))+endParen+' '
                    except TypeError:return [False,"BadArgument: '"+str(fofo)+"' for function '"+op+"'"]
            elif test[0]:
                # parse linear algebra function
                if arg1 in uservar: arg1=uservar[arg1]
                if arg2 in uservar: arg2=uservar[arg2]
                if arg3 in uservar: arg3=uservar[arg3]
                # print('We have:'+str(op)+' & '+str(arg1)+' & '+str(arg2)+' & '+str(arg3))
                try:res=adv_math(op,arg1,arg2,arg3)
                except UnboundLocalError: 
                    print("line 510ish. We got: "+str(op)+"/"+str(arg1)+"/"+str(arg2)+"/"+str(arg3)+". From "+str(arg)+" and "+str(arg15)+".")
                    return [False,"BadArguments: No arguments given to advanced function '"+str(op)+"'"]
                except NameError:
                    print("line 513ish. We got: "+str(op)+"/"+str(arg1)+"/"+str(arg2)+"/"+str(arg3)+".)")
                    print("From "+str(arg)+" and "+str(arg15)+",")
                    print(" with "+str(test))
                    return [False,"NameError"]
                except UnboundLocalError:
                    print("line 515ish. We got: "+str(op)+"/"+str(arg1)+"/"+str(arg2)+"/"+str(arg3)+". From "+str(arg)+" and "+str(arg15)+", with "+str(test)+" and "+str(res))
                    return [False,"ULE"]
                if res[0]==True: fparse+=result[1]+' '
                else: return res
            else: 
                #print('tested linalg on '+str(op))
                if op in binary: fparse+=op+' '
                elif op in numbers:fparse+=str(numbers[op])+' '
                elif op=='':pass
                else: 
                    if not test[0] and test[1]!='Skip': return test
                    elif not test[0]:
                        test=adv_math(op,'testfunction','force','')
                        if test[0]: 
                            if test[1]: 
                                return [False,"BadArguments: No enclosed arguments given to '"+str(op)+"'"]
                            elif not test[1]:
                                errorMsg="PackageError::NumPy: You can't do advanced functions without this package. (Also, BadArguments: No enclosed arguments given to '"+str(op)+"')"
                                import sys
                                if sys.version_info[0]>2: 
                                    errorMsg+=" (NumPy may not be released for this version of Python yet. Consider running an older version, like 2.6.5)"
                                import os
                                try:
                                    if os.uname()[0] == 'Linux':
                                        print('Attempting to install the package. You will have to retry your command.')
                                        os.system('sudo apt-get install python-numpy')
                                except:pass
                                return [False,errorMsg]
                            else: return [False,"BadFunction: '"+op+"'"]
                        else: return [False,"BadFunction: '"+op+"'"]
                    else: return [False,"BadFunction: '"+op+"'"]
        elif tensorTest>=0:
            #also handle straight-up function entry; for now just save tensor
            real_ret=parseTensor(string_in)
        elif op=='': pass
        elif op==')': fparse+=op
        elif n==1: 
            n-=1
            if op in binary: fparse+=op+' '
        else:fparse+=op+' '
        # in all cases, build a parsed string
        i+=1
        #print(op)
    try:
        if tensorTest>=0: fparse=''
    except NameError: tensorTest=-1
    #Now, parse the binary functions
    #print(fparse)
    #print(ops)
    pos=fparse.find("(")
    paren1=fparse.split('(')
    if len(paren1)>0:
        i=0
        pparse=resplit(paren1,")")
        #possibly loop to remove whitespace
        joiner=' '
    #no more parens of any kind; parse it all out
    if pos>0:
        #Only check out slices with %2=1
        for element in pparse:
            if i%2==1:
                pparse[i]=parseBinary(element)
            i+=1
        final=joiner.join(pparse)
    elif pos==0:
        #only check out slices with %2=0
        pparse.remove('')
        for element in pparse:
            if i%2==0:
                pparse[i]=parseBinary(element)
            i+=1
        final=joiner.join(pparse)
    else: final=pparse[0]
    retval=parseBinary(final)
    try: test=retval[0]
    except IndexError: 
        test=False
        retval=[True,'']
    else: test=True
    if is_numeric(retval) and not store: return [True,retval]
    elif is_numeric(retval) or tensorTest>=0: 
        global uservar
        if store not in manual and store not in binary: #does store have to be set?
            if tensorTest>=0: retval=real_ret
            uservar[store] = retval
        else: return [False,"StoreError: Variable '"+str(store)+"' is a reserved variable. Your result was "+str(retval)+"."]
        if retval[0]!=False: return [True,retval]
        else: return retval
    elif not test: return retval
    else: return [False,'UnknownError::LastComputeStep: '+str(retval)]
                
def parseBinary(eqn):
    #parse equation string with binary ops
    #break into paren'd then do
#    print(eqn)
#    if str(eqn).find("(")>=0:
#        stack1=str(eqn).split("(")
#        stack1=resplit(stack1,")")
#        whitespace=' '
#        print(eqn)
#        eqn=parseBinary(whitespace.join(stack1))
#        print(eqn)
    stack=str(eqn).split(' ')
    #first, fix negatives
    neg=0
    build=str(eqn)
    for element in stack:
        if element=='-':
            try:val=stack[neg-1]
            except IndexError: return [False,'BadNegative: '+build]
            except ValueError: return [False,'BadNegative: '+build]
            else:
                if is_numeric(val): pass
                elif val.find(")")>=0 or val.find("(")>=0 or val in binary or val in result or val=='':
                    try: val2=stack[neg+1]
                    except IndexError: return [False,'BadNegative::tooFewArgs: '+build]
                    else:
                        if val2 in numbers: val2=numbers[val2]
                        try: val2=float(str('-')+str(val2))
                        except ValueError: return [False,'BadNegative::notANumber: '+build]
                        else:
                            stack[neg]=''
                            stack[neg+1]=str(val2)
                else:
                    return [False,'BadNegative: '+build]
        neg+=1
    build=exponentiate(stack)
    bo=build
    stack=build.split(' ')
    looper=True
    while looper:
        looper=False
        for element in stack:
            if element == '^': looper=True
        if looper:
            build=exponentiate(stack)
            if bo==build: 
                try: float(build)
                except ValueError:return [False,'Invalid operand [^]']
                else: return build
            stack=build.split(' ')
    build=muldimod(stack)
    bo=build
    stack=build.split(' ')
    looper=True
    while looper:
        looper=False
        for element in stack:
            if element == '*' or element=='/' or element=='%': looper=True
        if looper:
            build=muldimod(stack)
            if bo==build: 
                try: float(build)
                except ValueError:return [False,'Invalid operand(s) [*,/,%]']
                else: return build
            stack=build.split(' ')
    build=addsub(stack)
    bo=build
    looper=True
    while looper:
        looper=False
        for element in stack:
            if element == '+' or element=='-': looper=True
        if looper:
            #print(stack)
            build=addsub(stack)
            #print(build)
            if bo==build: 
                try: float(build)
                except ValueError:
                    #see if can catch negative numbers
                    #traceback.print_last()
                    #print(build)
                    return [False,'Invalid operand(s) [+,-]']
                else: return build
            stack=build.split(' ')
    check=build.split(' ')
    repeat=False
    for element in check: 
        if element in binary: repeat=True
    if repeat: build=parseBinary(build)
    return build

def exponentiate(stack):
    build=''
    i=0
    n=0
    try: stack.remove('')
    except ValueError: pass
    for a in stack:
        if len(stack)>=3 and n==0 and a!='':
            try: a=float(a)
            except ValueError: build+=a+' '
            else:
                try: op=stack[i+1]
                except IndexError: 
                    build+=str(a)+' '
                else:
                    try: b=stack[i+2]
                    except IndexError: build+=str(a)+' '+str(op)
                    else:
                        try: b=float(b)
                        except ValueError: 
                            build+=str(a)+' '
                        else:
                            if op in binary:
                                if op == "^": 
                                    n=2
                                    try:build+=str(binary[op](a,b))+' '
                                    except TypeError: return [False,str(a)+op+str(b)]
                                else: build+=str(a)+' '
        elif len(stack)<3: build=stack[0]
        else: 
            if a!='':n-=1
        i+=1
    return build

def formatInput(string):
    string=string.replace("))",") )")
    out=string.split(' ')
    for key,value in binary.items():
        for element in out:
            if element.find(key) >=0: #Position zero is op only
                out=resplit(out,key,True) #keep resplitting as long as there are ops
    loop=True
    while loop:
        try:out.remove('')
        except ValueError: loop=False
        else: loop=True
    return out

def listfind(f, seq):
  for item in seq:
    if f(item):return item
    else: return False

def muldimod(stack):
    build=''
    i=0
    n=0
    try: stack.remove('')
    except ValueError: pass
    for a in stack:
        if len(stack)>=3 and n==0 and a!='':
            try: a=float(a)
            except ValueError: build+=str(a)+' '
            else:
                try: op=stack[i+1]
                except IndexError: 
                    build+=str(a)+' '
                else:
                    try: b=stack[i+2]
                    except IndexError: build+=str(a)+' '+str(op)
                    else:
                        try: b=float(b)
                        except ValueError: build+=str(a)+' '
                        else:
                            if op in binary:
                                if op == "*" or op=="/" or op=="%": 
                                    n=2
                                    try:build+=str(binary[op](a,b))+' '
                                    except TypeError: return [False,str(a)+op+str(b)]
                                else: build+=str(a)+' '
        elif len(stack)<3: build=stack[0]
        else: 
            if a!='':n-=1
        i+=1
    return build

def addsub(stack):
    build=''
    i=0
    n=0
    try: stack.remove('')
    except ValueError: pass
    for a in stack:
        if len(stack)>=3 and n==0 and a!='':
            try: a=float(a)
            except ValueError: build+=str(a)+' '
            else:
                try: op=stack[i+1]
                except IndexError: 
                    build+=str(a)+' '
                else:
                    try: b=stack[i+2]
                    except IndexError: build+=str(a)+' '+str(op)
                    else:
                        try: b=float(b)
                        except ValueError: build+=str(a)+' '
                        else:
                            if op in binary:
                                if op == "+" or op=="-": 
                                    n=2
                                    try:build+=str(binary[op](a,b))+' '
                                    except TypeError: return [False,str(a)+op+str(b)]
                                else: build+=str(a)+' '
        elif len(stack)<3: build=stack[0]
        else: 
            if a!='':n-=1
        i+=1
    return build


def resplit(arr,splitter,replace=False):
    i=0
    total=arr
    for element in arr:
        inew=element.find(splitter)
        if inew>=0:
            resplit=element.split(splitter)
            #print('Resplit: inputs '+str(total)+' outs '+str(resplit)+' with splitter '+str(splitter))
            if replace:
                temp=total
                # get the right spot
                search=resplit[0]+splitter+resplit[1]
                #print('Look for '+str(search))
                i=0
                for small in total:
                    if small.find(str(search))>=0: break
                    i+=1
                total=total[0:i]
                #print('Temp: '+str(temp))
                #print('Total: '+str(total))
                for peice in resplit:
                    total+=[peice]+list(splitter)
                    #print('Total currently: '+str(total))
                total=total[:-1]
                #print('Total currently: '+str(total))
                total+=temp[i+1:]
                #print('Total Out: '+str(total))
            else:total=total[0:i]+resplit+total[i+1:]
        i+=1
    return total

def is_numeric(s):
    try:
        i = float(s)
    except ValueError: return False
    except TypeError: return False
    except: return False
    else: return True

def sinh(x): 
    return (math.exp(x)-math.exp(-x))/2 

def cosh(x): 
    return (math.exp(x)+math.exp(-x))/2 

def tanh(x): 
    return sinh(x)/cosh(x) 

def asinh(x):
    return math.log(x+math.sqrt(math.pow(x,2)+1))

def acosh(x):
    if x>=1:
        return math.log(x+math.sqrt(math.pow(x,2)-1))
    else: return float('nan')

def atanh(x):
    if math.pow(x,2)<1:
        return .5*math.log((1+x)/(1-x))
    else: return float('nan')

def acsch(x):
    if x>0:return math.log((1+math.sqrt(1+math.pow(x,2)))/x)
    elif x<0: return math.log((1-math.sqrt(1+math.pow(x,2)))/x)
    else: return float('nan')
                        
def asech(x):
    if x>0 and x<=1:
        return math.log((1+math.sqrt(1-x^2))/x)
    else: return float('nan')

def acoth(x):
    if math.pow(x,2)>1: return .5*math.log((x+1)/(x-1))
    else: return float('nan')

def toBase2(x): 
#Dec to binary 
    return False


def toBase10(x): 
#binary to Dec 
    return False

#hex? 

def rpnmode(): 
#loop here till 'normmode' 
#handle stack 
    return False

def radianMode(x):
    global radians
    radians=True
    print("\nTrig mode is now radians\n")
    return 1

def degreeMode(x):
    global radians
    radians=False
    print("\nTrig mode is now degrees\n")
    return 1

def trigMode(arg):
    if not radians: 
        return math.pi*arg/180
    else: return arg

#from mail.python.org
def round_to_n(x, n):
    if n < 1:
        raise ValueError("number of significant digits must be >= 1")
    # Use %e format to get the n most significant digits, as a string.
    format = "%." + str(n-1) + "e"
    as_string = format % x
    return float(as_string)

def set_sigs(x):
    global sigfig
    try:sigfig=int(x)
    except ValueError: 
        if x == 'runtesttext': return False
        else: return 'Not an integer number of significant digits'
    else: return x


def adv_math(function,a,b,c,d='',e='',f=''):
    # handle advanced functions
    linalg = {
        'lsfit':lambda a,b,c:lsfit(a,b,c),
        }
    stats = {
        'stddev':lambda a,b,c:stddev(a,b,c),
        }
    graph = {
        'plot':lambda a,b,c:plotPoints(a,b,c),
        'graph':lambda a,b,c:plotPoints(a,b,c),
        }
    try: import numpy
    except ImportError: 
        if b=='force':
            if a=='testfunction':
                if function in linalg: 
                    return [True,False]
                elif function in stats: 
                    return [True,False]
                elif function in graph: 
                    return [True,False]
                else: 
                    return [False,False]
        errorMsg="PackageError::NumPy: You can't do advanced functions without this package."
        import sys
        if int(sys.version_info[0])>2: errorMsg+=" (NumPy may not be released for this version of Python yet. Consider running an older version, like 2.6.5)"
        import os
        try:
            if os.uname()[0] == 'Linux':
                print('Attempting to install the package. You will have to retry your command.')
                os.system('sudo apt-get install python-numpy')
        except: pass
        return [False,errorMsg]
    else:
        if a=='testfunction':
            if function in linalg: 
                return [True,True]
            elif function in stats: 
                return [True,True]
            elif function in graph: 
                return [True,True]
            else: 
                return [False,False]
        if function in linalg:
            try:res=linalg[function](a,b,c)
            except TypeError: return [False,"BadArguments::LinearAlgebra: One or more arguments were invalid."]
            else: return res
        elif function in stats:
            try:res=stats[function](a,b,c)
            except TypeError: return [False,"BadArguments::Statistics: One or more arguments were invalid."]
            else: return res
        elif function in graph:
            print("Starting graph procedures")
            try:
                import pylab
            except ImportError:
                errorMsg="PackageError::MatPlotLib-PyLab: You can't do plotting without this package."
                import sys
                if int(sys.version_info[0])>2: errorMsg+=" (MatPlotLib may not be released for this version of Python yet. Consider running an older version, like 2.6.5)"
                import os
                try:
                    if os.uname()[0] == 'Linux':
                        print('Attempting to install the package. You will have to retry your command.')
                        os.system('sudo apt-get install python-matplotlib')
                except: pass
                return [False,errorMsg]
            try:res=graph[function](a,b,c)
            except TypeError: return [False,"BadArguments::Graphing: One or more arguments were invalid."]
            else: 
                #print('No exceptions raised')
                return res
        else: return [False,"BadFunction::AdvancedFunctions: Unknown function '"+str(function)+"'"]



def parseTensor(tensor,mode='save'):
    # do the magic
    try: import numpy
    except ImportError: 
        errorMsg="PackageError::NumPy: You can't use tensors without this package."
        import sys
        if int(sys.version_info[0])>2: errorMsg+=" (NumPy may not be released for this version of Python yet. Consider running an older version, like 2.6.5)"
        import os
        try:
            if os.uname()[0] == 'Linux':
                print('Attempting to install the package. You will have to retry your command.')
                os.system('sudo apt-get install python-numpy')
        except: pass
        return [False,errorMsg]
    try:
        x=numpy.array(list(eval(tensor)),float)
    except SyntaxError: return [False,"ParseError::TensorError: Malformed tensor. Enter 'man tensor' for help."]
    except TypeError: return [False,"ParseError::TensorError: Tensor elements improperly formed. Enter 'man tensor' for help."]
    except ValueError: 
        return [False,"ParseError::TensorError: Internal datatype error."]
    except: return [False,"ParseError::TensorError: Unspecified error (given '"+str(tensor)+"')."]
    else:
        if mode=='save': return tensor
        elif mode=='work': return x
        else: return False



def lsfit(ind,dep,mode=1):
    #Least squares fitting. Default to linear.
    if is_numeric(mode): power=mode
    col=power+1
    x=indep
    y=depend.T
    eqm=numpy.asmatrix(numpy.ones((col,numpy.size(y,0))))
    power=1 # this will have a value when checked; this is bookkeeping
    #cases
    for exp in range(1,power):
        m=0
        for step in x:
            eqm[val,m]=step^exp
            m+=1
    eqmt=eqm.T
    alpha=eqmt**eqm
    beta=eqmt**y
    ainverse=eqmt.I
    fit_coef=ainverse**beta
    fit_vals=eqm**fit_coef
    resid=y-fit_vals
    
    m=numpy.size(eqm,1)
    n=numpy.size(eqm,0)
    ptot=numpy.cumsum(numpy.multiply(resid,resid))
    index=numpy.size(ptot)-1
    ssq=ptot[0,index]/(m-n)
    #vardc stuff
    indices=(n+1)*range(0,n)
    i=0
    for index in indices:
        vardc[i]=ssq*ainverse[index]
        i+=1
    cap=numpy.size(x)
    n=0
    covar=0
    sqxdiff=0
    sqydiff=0
    while n < cap:
        xdiff=(x[n]-numpy.mean(x))
        ydiff=(y[n]-numpy.mean(y))
        covar=covar+(xdiff*ydiff)
        sqxdiff=sqxdiff+xdiff^2
        sqydiff=sqydiff+ydiff^2
        n+=1
    lcorr=covar/math.sqrt(sqxdiff*sqydiff)
    covar=covar/cap
    ret_out="Fit Coefficients: "+str(fit_coef)+"\nStandard Deviation: "+str(math.sqrt(vardc))+"\nLinear Correlation: "+str(numpy.abs(lcorr)) #more
    return [False,'AdvOK',ret_out]

def stddev(actual,ideal):
    #standard deviation
    pass

def plotPoints(ind,dep,others):
    #plotting
    #psuedocall: plot(x,y,title,xtitle,ytitle,mode,style)
    print('Starting plot ...')
    lstyle={
        'line':'-',
        'dash':'--',
        'dash-dot':'-.',
        'dot':':',
        }
    modes=['line','scatter','hist','bar']
    opargs=[]
    pos=others.find(",")
    print('What we got was:')
    print(ind)
    print(dep)
    print(others)
    i=0
    while pos>=0:
        #print('Next: '+str(pos))
        temp=others[:pos]
        try:others=others[pos+1:]
        except IndexError: others=''
        #print(temp)
        opargs.append(temp)
        pos=others.find(",")
        i+=1
    opargs.append(others)
    i=0
    mode='line'
    style='line'
    tit=''
    xtit=''
    ytit=''
    print(opargs)
    for arg in opargs:
        if i==0: tit=arg
        if i==1: xtit=arg
        if i==2: ytit=arg
        if i==3:
            if arg in modes: mode=arg
        if i==4:
            print('Test linestyle')
            if arg in lstyle.items(): 
                print('Changed line style')
                style=arg
        print(arg)
        i+=1
    #print('Defined line types. Continuing ...')
    if is_numeric(ind): 
        import numpy
        #print('Creating range')
        step=float(ind)/1000
        #print('Steps')
        x=numpy.arange(0.0,float(ind)+step,step)
        #print('Created')
        #print(x)
    elif ind.find("->")>0:
        print('Found range')
        ra=ind.split("->")
        if is_numeric(ra[0]) and is_numeric(ra[1]):
            print('Range was numeric')
            import numpy
            ran=float(ra[1])-float(ra[0])
            if ran>0:
                print('Good range')
                step=float(ran)/1000
                x=numpy.arange(float(ra[0]),float(ra[1])+step,step)
                print('Made range')
            else: return [False,"PlotError: Bad X-Range."]
        else: return [False,"PlotError: Bad X-Range values."]
            
    else:
        print('Assigning range')
        x=parseTensor(ind,'work')
        if x[0]==False and not is_numeric(x[0]): return x
    # Parse the equation passed in
    try:brack=str(dep).find("[")
    except AttributeError: brack=-2
    print('Checked for brackets '+str(brack)+' in '+str(dep))
    if brack>=0: 
        print('Checking!')
        y=parseTensor(dep,'work')
        if y[0]==False and not is_numeric(y[0]): return y
        print('Tensor OK')
    elif brack==-2: y=dep
    else:
        #parse equation
        if dep.find('X')<0: return [False,"PlotError: Unable to parse dependant coordinates."]
        else:
            print('Beginning formula parser: '+dep)
            simple_replace= {
                'sin':'numpy.sin',
                'cos':'numpy.cos',
                'tan':'numpy.tan',
                'sinh':'numpy.sinh',
                'cosh':'numpy.cosh',
                'tanh':'numpy.tanh',
                'asin':'numpy.arcsin',
                'acos':'numpy.arccos',
                'atan':'numpy.arctan',
                'asinh':'numpy.arcsinh',
                'acosh':'numpy.arccosh',
                'atanh':'numpy.arctanh',
                'sqrt':'numpy.sqrt',
                'ln':'numpy.log',
                'log10':'numpy.log10',
                'pow':'numpy.power',
                'exp':'numpy.exp',
                'cot':'1/numpy.tan',
                'csc':'1/numpy.sin',
                'sec':'1/numpy.cos',
                'sech':'1/numpy.cosh',
                'csch':'1/numpy.sinh',
                'coth':'1/numpy.tanh',
                #etc - check http://www.scipy.org/Numpy_Functions_by_Category
                }
            print('Checking adv')
            adv_replace={
                #write these such that they return numpy args
                '^':lambda x,a:x+a,#dummy
                'mod':lambda x,a:x%a,#func
                'rem':lambda x,a:x%a, #func
                'root':lambda x,a:math.pow(x,1/a), #needs to be a func
                'log':lambda x,a:math.log(x,a), #needs to be a func
                'acot':lambda x:math.atan(trigMode(1/x)),#numpy.atan(1/
                'acsc':lambda x:math.asin(trigMode(1/x)),
                'asec':lambda x:math.acos(trigMode(1/x)),
                'acsch':lambda x:acsch(trigMode(x)),
                'asech':lambda x:asech(trigMode(x)),
                'acoth':lambda x:acoth(trigMode(x)),
                }
            #base=formatInput(dep)
            print('Splitting around "(": '+dep)
            base=str(dep).split("(") #leave most formatting to numpy interpreter
            print('Base1: '+str(base))
            for key,value in binary.items():
                if dep.find(key)>=0: base=resplit(base,key,True)
            # print(base)
            # for key,value in result.items():
            #     for element in base:
            #         print('Searching for '+str(key)+' in '+element)
            #         if element.find(key) >=0: #Position zero is op only
            #             base=resplit(base,key,True)
            i=0
            print('Base2: '+str(base))
            for element in base:
                if element in simple_replace: 
                    base[i]=simple_replace[element]+'('
                i+=1
            # also do adv_replace
            ready=''.join(base)
            print('Base3: '+str(base))
            # loop=True
            # while loop:
            #     try:ready=ready.replace('X','')
            #     except ValueError: loop=False
            #     else: loop=True
            ready=ready.replace('X','x')
            print('Test Function: '+str(ready))
            try: y=eval(ready)
            except: return [False,"PlotError: Malformed dependant function"]
    print('Starting pylab plot.')
    #print("Using style '"+str(lstyle[style])+"' via '"+str(style)+"'")
    #generate plot type based on mode; scatter, hist, bar, line
    import pylab
    try: pylab.plot(x, y,linestyle=lstyle[style])
    except: return [False,"PlotError: Unknown plot error"]
    #print('Wrote plot')
    pylab.xlabel(str(xtit))
    pylab.ylabel(str(ytit))
    #print('Assigned axes')
    pylab.title(str(tit))
    #print('Gave title')
    pylab.grid(True)
    #print('Made grid')
    #pylab.savefig('plot')
    pylab.show()
    #print('Showed')
    return [False,'AdvOK',"Plot completed."]



#run the thing!
print('\nPython Calculator 0.4.13')
print('\nLoading libraries ...')
try:import numpy
except:pass
print('\n\nKnown issues: Negative numbers in scientific notation are not valid.\n\n')
if radians: mode='Radians'
else: mode='Degrees'
print('Trig mode: '+mode+'\nSignificant figures: '+str(sigfig)+'\n')
print("Type 'help' for help.\n")
handler()
