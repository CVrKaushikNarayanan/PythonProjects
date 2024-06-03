import email
import imaplib
def e():  
    l=[]
    g=emailr()
    for j in g:
        u=j.split(',')
        x=''
        for k in u:
            for i in k:
                if i!='[' and i!="'" and i!=']':
                    x=x+i
        s=x.split()
        if len(s)==4:
            l.append(s)
    return l
        
    

def emailr():
    e = 'Your Gmail' 
    p = 'Password'
    s = 'imap.gmail.com'
    mail = imaplib.IMAP4_SSL(s)
    mail.login(e, p)
    mail.select('inbox')
    status, d = mail.search(None, 'ALL')
    mids = []
    imp=[]
    for b in d:
        mids += b.split()
    for i in mids:
        status, d = mail.fetch(i, '(RFC822)')
        for rt in d:
            if isinstance(rt, tuple):
                m = email.message_from_bytes(rt[1])
                mf = m['from']
                
                ms = m['subject']
                if m.is_multipart():
                    mc = ''
                    for p in m.get_payload():
                        mc += p.get_payload()
                else:
                    mc = m.get_payload()

                if mf == 'mr.mistakie@gmail.com':
                    imp.append(mc)
    return imp

