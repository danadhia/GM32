convoc = {'10':'ADD','11':'ADDC','12':'SUB','13':'SUBC','14':'AND','15':'OR','16':'XOR','17':'NOT','18':'SHL','19':'SHR','1A':'ROL','1B':'ROR'
          ,'20' : 'ADDI','21':'ADDCI','22':'SUBI','23':'SUBCI','24':'SHLI','25':'SHRI','26':'LDRI','27':'STRI','30':'NOT','32':'MOV','33':'SWP','34':'COMP','36':'LDR','37':'STR'
          ,'40':'MOVI','42':'COMPI','50':'B','51':'BEQ','52':'BNE','53':'BLT','54':'BGT','58':'BR','59':'BREQ','5A':'BRNE','5B':'BRLT','5C':'BRGT'
          ,'60':'BRI','61':'BRIEQ','62':'BRINE','63':'BRILT','64':'BRIGT','00':'NOP'}
def tohex(b):
    return format(b,'08X')
convreg =  {0: 'R0',1: 'R1',2: 'R2',3: 'R3',4: 'R4', 5: 'R5', 6: 'R6', 7: 'R7',8:'R8',9: 'R9', 10 : 'R10', 11: 'R11',12: 'R12',13: 'R13', 14: 'R14', 15: 'R15',16:''}
def printhasil():
    print('PC='+cnt,'IR='+inst,convoc[oc],convreg[op1],rg2,rg3)
    print('R0=0x'+tohex(reg[0]),'R1=0x'+tohex(reg[1]),'R2=0x'+tohex(reg[2]),'R3=0x'+tohex(reg[3]))
    print('R4=0x'+tohex(reg[4]),'R5=0x'+tohex(reg[5]),'R6=0x'+tohex(reg[6]),'R7=0x'+tohex(reg[7]))
    print('R8=0x'+tohex(reg[8]),'R9=0x'+tohex(reg[9]),'R10=0x'+tohex(reg[10]),'R11=0x'+tohex(reg[11]))
    print('R12=0x'+tohex(reg[12]),'R13=0x'+tohex(reg[13]),'R14=0x'+tohex(reg[14]),'R15=0x'+tohex(reg[15]),'\n')
reg=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
rom=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
code_file=open("instruction code.bin","r")
data = code_file.readlines()
code_file.close()
data = [a.strip() for a in [ x for x in data ]]
data = [a.split(' ') for a in [ x for x in data ]]
PC=0
while PC<len(data) :
    cont=data[PC]
    cnt='%s' %cont[0]
    inst='%s' %cont[1]
    PC=PC+1
    oc=inst[slice(2,4,1)]
    op1=int(inst[slice(4,5,1)],16)
    op2=int(inst[slice(5,6,1)],16)
    op3=int(inst[slice(6,7,1)],16)
    if oc[slice(1)]=="1":
        rg2=convreg[op2]
        rg3=convreg[op3]
        if oc=='10':
            reg[op1]=reg[op2]+reg[op3]
##        elif oc=='11':
##            reg[op1]=reg[op2]+reg[op3]+c
        elif oc=="12":
            reg[op1]=reg[op2]-reg[op3]
##        elif oc=='13'
##            reg[op1]=reg[op2]-reg[op3]-c
        elif oc=='14':
            reg[op1]=reg[op2]&reg[op3]
        elif oc=='15':
            reg[op1]=reg[op2]|reg[op3]
        elif oc=='16':
            reg[op1]=reg[op2]^reg[op3]
        elif oc=='17':
            reg[op1]=reg[op2]+reg[op3]
        elif oc=='18':
            reg[op1]=reg[op2]<<reg[op3]
        elif oc=='19':
            reg[op1]=reg[op2]>>reg[op3]
        elif oc=='1A':
            reg[op1]=(reg[op2]<<reg[op3])|(reg[op2]>>(32-reg[op3]))
        elif oc=='1B':
            reg[op1]=(reg[op2]>>reg[op3])|(reg[op2]<<(32-reg[op3]))
    elif oc[slice(1)]=="2":
        op3=int(inst[slice(6,11,1)],16)
        rg2=convreg[op2]
        rg3='#'+format(op3,'#06X')
        if oc=="20":
            reg[op1]=reg[op2]+op3
##        elif oc=="21":
##            reg[op1]=reg[op2]+op3+c
        elif oc=="22":
            reg[op1]=reg[op2]-op3
##        elif oc=="23":
##            reg[op1]=reg[op2]-op3-c
        elif oc=="24":
            reg[op1]=reg[op2]<<op3
        elif oc=="25":
            reg[op1]=reg[op2]>>op3
        elif oc=="26":
            reg[op1]=rom[op2]+op3
        elif oc=="27":
            rom[op1]=reg[op2]-op3
    elif oc[slice(1)]=="3":
        rg2=convreg[op2]
        rg3=''
        if oc=="32":
            reg[op1]=reg[op2]
        elif oc=="30":
            reg[op1]=reg[op2]^0XFFFFFFFF
        elif oc=="33":
            reg[op1],reg[op2]=reg[op2],reg[op1]
        elif oc=="34":
            if (reg[op1]-reg[op2])<0 :
                z,n=0,1
            else:
                z,n=1,0
        elif oc=="36":
            reg[op1]=rom[op2]
        elif oc=="37":
            rom[op1]=reg[op2]
    elif oc[slice(1)]=="4":
        op3=int(inst[slice(6,11,1)],16)
        rg2=''
        rg3='#'+format(op3,'#06X')
        if oc=="40":
            reg[op1]=op3
        elif oc=="42":
            if (reg[op1]-op3)<0 :
                z,n=0,1
            else:
                z,n=1,0
    elif oc[slice(1)]=="5":
        rg2,rg3='',''
        if oc=="50":
            PC=reg[op1]-1
        elif oc=='51':
            if z==1:
                PC=reg[op1]-1
        elif oc=='52':
            if z==0:
                PC=reg[op1]-1
        elif oc=='53':
            if n==1:
                PC=reg[op1]-1
        elif oc=='54':
            if n==0:
                PC=reg[op1]-1
        elif oc=="58":
            PC=PC+reg[op1]-1
        elif oc=='59':
            if z==1:
                PC=PC+reg[op1]-1
        elif oc=='5A':
            if z==0:
                PC=PC+reg[op1]-1
        elif oc=='5B':
            if n==1:
                PC=PC+reg[op1]-1
        elif oc=='5C':
            if n==0:
                PC=PC+reg[op1]-1
    elif oc[slice(1)]=="6":
        op1=16
        op3=int(inst[slice(4,11,1)],16)
        rg2=''
        rg3='#'+format(op3,'#08X') 
        if oc=="60":
            PC=PC+op3-1
        elif oc=='61':
            if z==1:
                PC=PC+op3-1
        elif oc=='62':
            if z==0:
                PC=PC+op3-1
        elif oc=='63':
            if n==1:
                PC=PC+op3-1
        elif oc=='64':
            if n==0:
                PC=PC+op3-1
    else:
        oc,op1='00',16
        rg2,rg3='',''
    printhasil()
