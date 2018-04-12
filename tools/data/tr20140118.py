#                                                         -*- coding: utf-8 -*-
#! \file    ./tools/data/tr20140118.py
#! \author  Jiří Kučera, <jkucera AT redhat.com>
#! \stamp   2018-04-10 01:23:17 (UTC+01:00, DST+01:00)
#! \project passwd maintenance tools
#! \license MIT
#! \version 0.0.0
#! \fdesc   Translation data.
#


def setup(t25l):
    pofiles = t25l.PoFileSet()
    po = t25l.PoFile.from_scratch("de")
    po.additem("""\
#: libuser.c:91
#, c-format
msgid "%s: libuser initialization error:"
msgstr "%s: libuser Initialisierungs-Fehler:"
    """)
    po.additem("""\
#: libuser.c:267
msgid "Corrupted passwd entry."
msgstr "Beschädigte Passwort-Eintragung."
    """)
    po.additem("""\
#: libuser.c:284
msgid "Empty password."
msgstr "Leeres Passwort."
    """)
    po.additem("""\
#: libuser.c:305
msgid "Alternate authentication scheme in use."
msgstr "Alternatives Autentifizierungs-Muster wird verwendet"
    """)
    po.additem("""\
#: libuser.c:310
msgid "Password set, DES crypt."
msgstr "Passwort mit DES-Verschlüsselung gesetzt."
    """)
    po.additem("""\
#: libuser.c:323
#, c-format
msgid "No password set.\\n"
msgstr "Kein Passwort gesetzt.\\n"
    """)
    po.additem("""\
#: libuser.c:328
#, c-format
msgid "Unknown user.\\n"
msgstr "Unbekannter Benutzer.\\n"
    """)
    po.additem("""\
#: passwd.c:157
msgid "keep non-expired authentication tokens"
msgstr "behalte nicht-verfallende Authentifizierungs-Merkmale"
    """)
    po.additem("""\
#: passwd.c:159
msgid "delete the password for the named account (root only)"
msgstr "lösche das Passwort für das angegebene Konto (nur als root möglich)"
    """)
    po.additem("""\
#: passwd.c:162
msgid "lock the password for the named account (root only)"
msgstr "Das Kennwort für das angegebene Konto sperren (nur root)"
    """)
    po.additem("""\
#: passwd.c:165
msgid "unlock the password for the named account (root only)"
msgstr "Das Kennwort für das angegebene Konto entsperren (nur root)"
    """)
    po.additem("""\
#: passwd.c:168
msgid "expire the password for the named account (root only)"
msgstr "Das Kennwort für das angegebene Konto verfallen lassen (nur root)"
    """)
    po.additem("""\
#: passwd.c:177
msgid ""
"number of days warning users receives before password expiration (root only)"
msgstr ""
"Anzahl der Tage die Benutzer vor dem Ablauf des Passwortes gewarnt werden "
"soll (nur als root möglich)"
    """)
    po.additem("""\
#: passwd.c:183
msgid "report password status on the named account (root only)"
msgstr "melde Passwort Status des angegebenen Accounts (nur als root möglich)"
    """)
    po.additem("""\
#: passwd.c:266
#, c-format
msgid "%s: Cannot mix one of -l, -u, -d, -S and one of -i, -n, -w, -x.\\n"
msgstr ""
"%s: Die Parameter -l, -u, -d, -S und -i, -n, -w, -x können nicht kombiniert "
"werden.\\n"
    """)
    po.additem("""\
#: passwd.c:335
#, c-format
msgid "%s: Can not identify you!\\n"
msgstr "%s: Kann Sie nicht identifizieren!\\n"
    """)
    po.additem("""\
#: passwd.c:388
#, c-format
msgid "%s: SELinux denying access due to security policy.\\n"
msgstr ""
"%s: SELinux verweigert den Zugriff aufgrund der Sicherheitsrichtlinien.\\n"
    """)
    po.additem("""\
#: passwd.c:398
#, c-format
msgid "Locking password for user %s.\\n"
msgstr "Sperren Passwort für Benutzer %s.\\n"
    """)
    po.additem("""\
#: passwd.c:402 passwd.c:414 passwd.c:429 passwd.c:440 passwd.c:458
msgid "Success"
msgstr "Erfolgreich"
    """)
    po.additem("""\
#: passwd.c:410
#, c-format
msgid "Unlocking password for user %s.\\n"
msgstr "Entsperren Passwort für Benutzer %s.\\n"
    """)
    po.additem("""\
#: passwd.c:416
msgid "Unsafe operation (use -f to force)"
msgstr "Unsichere Operation (benutzen Sie -f zum Erzwingen)"
    """)
    po.additem("""\
#: passwd.c:425
#, c-format
msgid "Expiring password for user %s.\\n"
msgstr "Passwort für Benutzer %s verfallen lassen.\\n"
    """)
    po.additem("""\
#: passwd.c:437
#, c-format
msgid "Removing password for user %s.\\n"
msgstr "Entfernen Passwort für Benutzer %s.\\n"
    """)
    po.additem("""\
#: passwd.c:455
#, c-format
msgid "Adjusting aging data for user %s.\\n"
msgstr "justieren Verfallsdaten für Benutzer %s.\\n"
    """)
    po.additem("""\
#: passwd.c:471
#, c-format
msgid "Changing password for user %s.\\n"
msgstr "Ändern Passwort für Benutzer %s.\\n"
    """)
    po.additem("""\
#: passwd.c:553
#, c-format
msgid "%s: expired authentication tokens updated successfully.\\n"
msgstr ""
"%s: abgelaufene Authentifizierungs-Merkmale erfolgreich aktualisiert.\\n"
    """)
    po.additem("""\
#: passwd.c:556
#, c-format
msgid "%s: all authentication tokens updated successfully.\\n"
msgstr "%s: alle Authentifizierungs-Merkmale erfolgreich aktualisiert.\\n"
    """)
    pofiles.add(po)
    po = t25l.PoFile.from_scratch("es")
    po.additem("""\
#: libuser.c:300
msgid "Password set, SHA512 crypt."
msgstr "Contraseña establecida, cifrado SHA512."
    """)
    po.additem("""\
#: libuser.c:403
#, c-format
msgid "%s: user account has no support for password aging.\\n"
msgstr ""
"%s: la cuenta del usuario no tiene soporte para envejecimiento de contraseña."
"\\n"
    """)
    po.additem("""\
#: passwd.c:157
msgid "keep non-expired authentication tokens"
msgstr "mantener las marcas de autenticación no vencidos"
    """)
    po.additem("""\
#: passwd.c:165
msgid "unlock the password for the named account (root only)"
msgstr "desbloquear la contraseña para la cuenta indicada (solo root)"
    """)
    po.additem("""\
#: passwd.c:186
msgid "read new tokens from stdin (root only)"
msgstr "leer símbolos nuevos desde stdin (solo root)"
    """)
    po.additem("""\
#: passwd.c:193
msgid "[OPTION...] <accountName>"
msgstr "[OPCIÓN...] <accountName>"
    """)
    po.additem("""\
#: passwd.c:539
#, c-format
msgid "%s: unable to set failure delay: %s\\n"
msgstr "%s: no se pudo establecer la espera máxima para fallo: %s\\n"
    """)
    po.additem("""\
#: passwd.c:553
#, c-format
msgid "%s: expired authentication tokens updated successfully.\\n"
msgstr "%s: símbolos de autenticación vencidos actualizados con éxito.\\n"
    """)
    po.additem("""\
#: passwd.c:556
#, c-format
msgid "%s: all authentication tokens updated successfully.\\n"
msgstr "%s: todos los símbolos de autenticación se actualizaron con éxito.\\n"
    """)
    pofiles.add(po)
    po = t25l.PoFile.from_scratch("gu")
    po.additem("""\
#: passwd.c:162
msgid "lock the password for the named account (root only)"
msgstr "નામવાળા ખાતા માટે પાસવર્ડને તાળું મારો (માત્ર રુટ)"
    """)
    po.additem("""\
#: passwd.c:165
msgid "unlock the password for the named account (root only)"
msgstr "નામવાળા ખાતા માટે પાસવર્ડનું તાળું ખોલો (માત્ર રુટ)"
    """)
    po.additem("""\
#: passwd.c:168
msgid "expire the password for the named account (root only)"
msgstr "નામવાળા ખાતા માટે પાસવર્ડ નિવૃત્ત (માત્ર રુટ)"
    """)
    po.additem("""\
#: passwd.c:177
msgid ""
"number of days warning users receives before password expiration (root only)"
msgstr ""
"પાસવર્ડ સમયસમાપ્તિ પહેલાં વપરાશકર્તાઓ ચેતવણી મેળવે તે દિવસોની સંખ્યા (માત્ર "
"રુટ)"
    """)
    po.additem("""\
#: passwd.c:180
msgid ""
"number of days after password expiration when an account becomes disabled "
"(root only)"
msgstr ""
"પાસવર્ડ સમયસમાપ્ત થાય પછી જ્યારે ખાતું નિષ્ક્રિય બની જાય તે દિવસોની સંખ્યા "
"(માત્ર રુટ)"
    """)
    po.additem("""\
#: passwd.c:388
#, c-format
msgid "%s: SELinux denying access due to security policy.\\n"
msgstr "%s: સુરક્ષા પૉલીસિના કારણે SELinux વપરાશ નામંજૂર કરી રહ્યું છે.\\n"
    """)
    po.additem("""\
#: passwd.c:425
#, c-format
msgid "Expiring password for user %s.\\n"
msgstr "વપરાશકર્તા %s માટે પાસવર્ડ નિવૃત્ત થઇ રહ્યો છે.\\n"
    """)
    pofiles.add(po)
    po = t25l.PoFile.from_scratch("hi")
    po.additem("""\
#: libuser.c:403
#, c-format
msgid "%s: user account has no support for password aging.\\n"
msgstr ""
"%s: उपयोक्ता खाता के खाते में शब्दकूट एजिंग के लिये कोई समर्थन नहीं है.\\n"
    """)
    po.additem("""\
#: passwd.c:162
msgid "lock the password for the named account (root only)"
msgstr "नामित खाता के लिये कूटशब्द लॉक करें (सिर्फ रूट)"
    """)
    po.additem("""\
#: passwd.c:165
msgid "unlock the password for the named account (root only)"
msgstr "नामित खाता के लिये कूटशब्द अनलॉक करें (सिर्फ रूट)"
    """)
    po.additem("""\
#: passwd.c:168
msgid "expire the password for the named account (root only)"
msgstr "नामित खाता के लिये कूटशब्द समय समाप्त करें (सिर्फ रूट)"
    """)
    po.additem("""\
#: passwd.c:177
msgid ""
"number of days warning users receives before password expiration (root only)"
msgstr ""
"शब्दकूट के समय समाप्त होने के लिये पहले उपयोक्ता प्राप्त करता है दिनों की "
"संख्या (रूट सिर्फ)"
    """)
    po.additem("""\
#: passwd.c:180
msgid ""
"number of days after password expiration when an account becomes disabled "
"(root only)"
msgstr ""
"शब्दकूट समय समाप्ति के बाद दिनों की संख्या जब एक खाता निष्क्रिय हो जाता है "
"(सिर्फ रूट)"
    """)
    po.additem("""\
#: passwd.c:388
#, c-format
msgid "%s: SELinux denying access due to security policy.\\n"
msgstr "%s: SELinux सुरक्षा नीति के कारण पहुँच को मना कर रहा है.\\n"
    """)
    po.additem("""\
#: passwd.c:425
#, c-format
msgid "Expiring password for user %s.\\n"
msgstr "%s उपयोक्ता के लिए कूटशब्द समाप्त हो रहा है.\\n"
    """)
    pofiles.add(po)
    po = t25l.PoFile.from_scratch("ml")
    po.additem("""\
#: passwd.c:159
msgid "delete the password for the named account (root only)"
msgstr ""
"പറഞ്ഞിരിക്കുന്ന അക്കൌണ്ടിന് പാസ്‌വേറ്‍ഡ് നീക്കം ചെയ്യുക (root-ന് മാത്റം "
"അധികാരമുള്ളൂ)"
    """)
    po.additem("""\
#: passwd.c:162
msgid "lock the password for the named account (root only)"
msgstr "പറഞ്ഞ അക്കൌണ്ടിനുള്ള രഹസ്യവാക്ക് പൂട്ടൂക (റൂട്ട് മാത്രം)"
    """)
    po.additem("""\
#: passwd.c:165
msgid "unlock the password for the named account (root only)"
msgstr "പറഞ്ഞ അക്കൌണ്ടിനുള്ള രഹസ്യവാക്ക് ലഭ്യമാക്കുക (റൂട്ട് മാത്രം)"
    """)
    po.additem("""\
#: passwd.c:168
msgid "expire the password for the named account (root only)"
msgstr ""
"പറഞ്ഞ അക്കൌണ്ടിനുള്ള രഹസ്യവാക്കിന്റെ കാലാവധി പൂര്‍ത്തിയാക്കുക (റൂട്ട് "
"മാത്രം)"
    """)
    po.additem("""\
#: passwd.c:173
msgid "maximum password lifetime (root only)"
msgstr ""
"പാസ്‌വേറ്‍ഡിനുളള ഏറ്റവും കൂടുതല്‍ കാലാവധി (root-ന് മാത്റം അധികാരമുള്ളൂ)"
    """)
    po.additem("""\
#: passwd.c:177
msgid ""
"number of days warning users receives before password expiration (root only)"
msgstr ""
"പാസ്‌വേറ്‍ഡിന്‍റെ കാലാവധി അവസാനിക്കുന്നതിന് മുന്പ് യൂസറുകള്‍ക്ക് എത്റ ദിവസം "
"മുന്നറിയിപ്പ് ലഭിക്കുന്നു (root-ന് മാത്റം അധികാരമുള്ളൂ)"
    """)
    po.additem("""\
#: passwd.c:180
msgid ""
"number of days after password expiration when an account becomes disabled "
"(root only)"
msgstr ""
"പാസ്‌വേറ്‍ഡിന്‍റെ കാലാവധി അവസാനിച്ച ശേഷം യൂസറിന്‍റെ അക്കൌണ്ട് എത്റ "
"ദിവസത്തിന് ശേഷംപ്റവറ്‍ത്തന രഹിതമാകുന്നു (root-ന് മാത്റം അധികാരമുള്ളൂ)"
    """)
    po.additem("""\
#: passwd.c:183
msgid "report password status on the named account (root only)"
msgstr ""
"പറഞ്ഞിരിക്കുന്ന അക്കൌണ്ടില്‍ പാസ്‌വേറ്‍ഡിന്‍റെ നിലവാരം വ്യക്തമാക്കുക (root-"
"ന് മാത്റം അധികാരമുള്ളൂ)"
    """)
    po.additem("""\
#: passwd.c:186
msgid "read new tokens from stdin (root only)"
msgstr ""
"stdin-ല്‍ നിന്നും പുതിയ ടോക്കനുകള്‍ ലഭ്യമാക്കുക (root-ന് മാത്റം "
"അധികാരമുള്ളൂ)"
    """)
    po.additem("""\
#: passwd.c:266
#, c-format
msgid "%s: Cannot mix one of -l, -u, -d, -S and one of -i, -n, -w, -x.\\n"
msgstr ""
"%s: -l, -u, -d, -S എന്നിവയില്‍ ഒന്ന് -i, -n, -w, -x എന്നിവയായി ചേറ്‍ത്ത് "
"നല്‍കുവാന്‍ സാധ്യമല്ല.\\n"
    """)
    po.additem("""\
#: passwd.c:388
#, c-format
msgid "%s: SELinux denying access due to security policy.\\n"
msgstr "%s: സുരക്ഷ സംവിധാനം കാരണം SELinux പ്രവേശനം നിഷേധിയ്ക്കുന്നു.\\n"
    """)
    po.additem("""\
#: passwd.c:416
msgid "Unsafe operation (use -f to force)"
msgstr ""
"പാടില്ലാത്ത പ്റക്റിയ (നിറ്‍ബന്ധപൂറ്‍വ്വം ചെയ്യുന്നതിന് -f ഉപയോഗിക്കുക)"
    """)
    po.additem("""\
#: passwd.c:425
#, c-format
msgid "Expiring password for user %s.\\n"
msgstr "%s ഉപയോക്താവിനുള്ള രഹസ്യവാക്കിന്റെ കാലാവധി അവസാനിയ്ക്കുന്നു.\\n"
    """)
    po.additem("""\
#: passwd.c:553
#, c-format
msgid "%s: expired authentication tokens updated successfully.\\n"
msgstr ""
"%s: കാലാവധി കഴിഞ്ഞ ഓഥന്‍റിക്കേഷന്‍ ടോക്കനുകള്‍ വിജയകരമായി "
"പുതുക്കിയിരിക്കുന്നു.\\n"
    """)
    po.additem("""\
#: passwd.c:556
#, c-format
msgid "%s: all authentication tokens updated successfully.\\n"
msgstr ""
"%s: എല്ലാ ഓഥന്‍റിക്കേഷന്‍ ടോക്കനുകളും വിജയകരമായി പുതുക്കിയിരിക്കുന്നു.\\n"
    """)
    pofiles.add(po)
    po = t25l.PoFile.from_scratch("mr")
    po.additem("""\
#: passwd.c:162
msgid "lock the password for the named account (root only)"
msgstr "नाव दिलेल्या खात्याकरिता पासवर्ड कुलूपबंद करा (फक्त रूट)"
    """)
    po.additem("""\
#: passwd.c:165
msgid "unlock the password for the named account (root only)"
msgstr "नाव दिलेल्या खात्याकरिता पासवर्ड खुले करा (फक्त रूट)"
    """)
    po.additem("""\
#: passwd.c:168
msgid "expire the password for the named account (root only)"
msgstr "नाव दिलेल्या खात्याकरिता पासवर्डची वेळ समाप्ति करा (फक्त रूट)"
    """)
    po.additem("""\
#: passwd.c:177
msgid ""
"number of days warning users receives before password expiration (root only)"
msgstr ""
"गुप्तशब्द मुदत समाप्तीच्या पहिले वापरकर्त्यांना काहिक दिवसांची सावधानता "
"मिळते (फक्त रूट)"
    """)
    po.additem("""\
#: passwd.c:388
#, c-format
msgid "%s: SELinux denying access due to security policy.\\n"
msgstr "%s: सुरक्षा करारमुळे SELinux प्रवेश नकारत आहे.\\n"
    """)
    po.additem("""\
#: passwd.c:425
#, c-format
msgid "Expiring password for user %s.\\n"
msgstr "वापरकर्ता %s करिता पासवर्डची वेळसमाप्ति झाली.\\n"
    """)
    pofiles.add(po)
    po = t25l.PoFile.from_scratch("or")
    po.additem("""\
#: passwd.c:162
msgid "lock the password for the named account (root only)"
msgstr "ଏହି ନାମର ଖାତା ପାଇଁ ପ୍ରବେଶ ସଂକେତକୁ ଅପରିବର୍ତ୍ତନୀୟ କରନ୍ତୁ (କେବଳ ରୁଟ)"
    """)
    po.additem("""\
#: passwd.c:165
msgid "unlock the password for the named account (root only)"
msgstr "ଏହି ନାମର ଖାତା ପାଇଁ ପ୍ରବେଶ ସଂକେତକୁ ଖୋଲନ୍ତୁ (କେବଳ ରୁଟ)"
    """)
    po.additem("""\
#: passwd.c:168
msgid "expire the password for the named account (root only)"
msgstr "ଏହି ନାମର ଖାତା ପାଇଁ ପ୍ରବେଶ ସଂକେତର ସମୟ ସମାପ୍ତି ହୋଇଛି (କେବଳ ରୁଟ)"
    """)
    po.additem("""\
#: passwd.c:177
msgid ""
"number of days warning users receives before password expiration (root only)"
msgstr ""
"ପ୍ରବେଶ ସଙ୍କେତ ଅକାମି ହେବା ପୂର୍ବରୁ କେତେ ଦିନ ପର୍ଯ୍ଯନ୍ତ ଚାଳକ ଚେତାବନୀ ପ୍ରାପ୍ତ "
"କରିବ (କେବଳ ରୁଟ)"
    """)
    po.additem("""\
#: passwd.c:180
msgid ""
"number of days after password expiration when an account becomes disabled "
"(root only)"
msgstr ""
"ପ୍ରବେଶ ସଙ୍କେତ ଅକାମି ହେବା ପରେ କେତେ ଦିନ ପରେ ଖାତାଟି ନିଷ୍କ୍ରିୟ ହୋଇଯିବ (କେବଳ ରୁଟ)"
    """)
    po.additem("""\
#: passwd.c:266
#, c-format
msgid "%s: Cannot mix one of -l, -u, -d, -S and one of -i, -n, -w, -x.\\n"
msgstr ""
"%s: -l, -u, -d, -S ମଧ୍ଯରୁ ଗୋଟିଏ ଏବଂ  -i, -n, -w, -x ମଧ୍ଯରୁ ଗୋଟିଏକୁ ମିଶାଇ ହେବ "
"ନାହିଁ।\\n"
    """)
    po.additem("""\
#: passwd.c:388
#, c-format
msgid "%s: SELinux denying access due to security policy.\\n"
msgstr "%s: SELinux ସୁରକ୍ଷା ଦୃଷ୍ଟିକୋଣରୁ ପ୍ରବେଶ ବାରଣ କରିଛି।\\n"
    """)
    po.additem("""\
#: passwd.c:425
#, c-format
msgid "Expiring password for user %s.\\n"
msgstr "ବ୍ୟବହାରକାରୀ %s ପାଇଁ ପ୍ରବେଶ ସଂକେତର ସମୟ ସମାପ୍ତି ହେଉଛି।\\n"
    """)
    po.additem("""\
#: passwd.c:553
#, c-format
msgid "%s: expired authentication tokens updated successfully.\\n"
msgstr ""
"%s: ଅକାମ ହୋଇଯାଇଥିବା ବୈଧିକୃତ ଟୋକେନ ମାନଙ୍କୁ ସଫଳତାର ସହିତ ଅଦ୍ଯତିତ କରାଯାଇଛି।\\n"
    """)
    pofiles.add(po)
    po = t25l.PoFile.from_scratch("pa")
    po.additem("""\
#: libuser.c:157
msgid "Warning: unlocked password would be empty."
msgstr "ਚੇਤਾਵਨੀ: ਗੈਰ-ਤਾਲਾਬੰਦ ਗੁਪਤ-ਸ਼ਬਦ ਖਾਲੀ ਹੋਵੇਗਾ।"
    """)
    po.additem("""\
#: libuser.c:267
msgid "Corrupted passwd entry."
msgstr "ਨਕਾਰਾ ਗੁਪਤ-ਸ਼ਬਦ ਇੰਦਰਾਜ ਹੈ।"
    """)
    po.additem("""\
#: libuser.c:284
msgid "Empty password."
msgstr "ਖਾਲੀ ਗੁਪਤ-ਸ਼ਬਦ।"
    """)
    po.additem("""\
#: libuser.c:287
msgid "Password locked."
msgstr "ਗੁਪਤ-ਸ਼ਬਦ ਤਾਲਾਬੰਦ ਹੈ।"
    """)
    po.additem("""\
#: libuser.c:291
msgid "Password set, MD5 crypt."
msgstr "ਗੁਪਤ-ਸ਼ਬਦ ਦਿੱਤਾ, MD੫ ਕ੍ਰਿਪਟ।"
    """)
    po.additem("""\
#: libuser.c:294
msgid "Password set, blowfish crypt."
msgstr "ਗੁਪਤ-ਸ਼ਬਦ ਦਿੱਤਾ, blowfish ਕ੍ਰਿਪਟ।"
    """)
    po.additem("""\
#: libuser.c:297
msgid "Password set, SHA256 crypt."
msgstr "ਗੁਪਤ-ਸ਼ਬਦ ਸੈੱਟ, SHA256 ਕ੍ਰਿਪਟ।"
    """)
    po.additem("""\
#: libuser.c:300
msgid "Password set, SHA512 crypt."
msgstr "ਗੁਪਤ-ਸ਼ਬਦ ਸੈੱਟ, SHA256 ਕ੍ਰਿਪਟ।"
    """)
    po.additem("""\
#: libuser.c:302
msgid "Password set, unknown crypt variant."
msgstr "ਗੁਪਤ-ਸ਼ਬਦ ਦਿੱਤਾ, ਅਣਜਾਣ ਕ੍ਰਿਪਟ ਗੁਣ ਹੈ।"
    """)
    po.additem("""\
#: libuser.c:305
msgid "Alternate authentication scheme in use."
msgstr "ਬਦਲਵੀਂ ਪਰਮਾਣਿਕਤਾ ਤਰਕੀਬ ਵਰਤੋਂ ਵਿੱਚ।"
    """)
    po.additem("""\
#: libuser.c:310
msgid "Password set, DES crypt."
msgstr "ਗੁਪਤ-ਸ਼ਬਦ ਦਿੱਤਾ, DES ਕ੍ਰਿਪਟ।"
    """)
    po.additem("""\
#: libuser.c:323
#, c-format
msgid "No password set.\\n"
msgstr "ਕੋਈ ਗੁਪਤ-ਸ਼ਬਦ ਨਹੀਂ ਦਿੱਤਾ।\\n"
    """)
    po.additem("""\
#: libuser.c:328
#, c-format
msgid "Unknown user.\\n"
msgstr "ਅਣਪਛਾਤਾ ਯੂਜ਼ਰ\\n"
    """)
    po.additem("""\
#: libuser.c:403
#, c-format
msgid "%s: user account has no support for password aging.\\n"
msgstr "%s: ਯੂਜ਼ਰ ਖਾਤੇ ਕੋਲ ਗੁਪਤ-ਸ਼ਬਦ ਦੀ ਮਿਆਦ ਲਈ ਕੋਈ ਸਮਰਥਨ ਨਹੀਂ ਹੈ।\\n"
    """)
    po.additem("""\
#: passwd.c:157
msgid "keep non-expired authentication tokens"
msgstr "ਮਿਆਦ ਨਾ ਪੁੱਗੇ ਪਰਮਾਣਿਕਤਾ ਟੋਕਨ ਰੱਖੋ"
    """)
    po.additem("""\
#: passwd.c:159
msgid "delete the password for the named account (root only)"
msgstr " ਦਿੱਤੇ ਗਏ ਨਾਂ ਵਾਲੇ ਖਾਤੇ ਲਈ ਗੁਪਤ-ਸ਼ਬਦ ਮਿਟਾਉ(ਸਿਰਫ ਰੂਟ)"
    """)
    po.additem("""\
#: passwd.c:162
msgid "lock the password for the named account (root only)"
msgstr "ਦਿੱਤੇ ਗਏ ਨਾਂ ਵਾਲੇ ਵਾਲੇ ਖਾਤੇ ਲਈ ਗੁਪਤ-ਸ਼ਬਦ ਨੂੰ ਤਾਲਾਬੰਦ ਕਰੋ (ਸਿਰਫ ਰੂਟ)"
    """)
    po.additem("""\
#: passwd.c:165
msgid "unlock the password for the named account (root only)"
msgstr "ਦਿੱਤੇ ਗਏ ਨਾਂ ਵਾਲੇ ਖਾਤੇ ਲਈ ਗੁਪਤ-ਸ਼ਬਦ ਦਾ ਤਾਲਾ ਖੋਲ੍ਹੋ (ਸਿਰਫ ਰੂਟ)"
    """)
    po.additem("""\
#: passwd.c:168
msgid "expire the password for the named account (root only)"
msgstr "ਦਿੱਤੇ ਗਏ ਨਾਂ ਵਾਲੇ ਖਾਤੇ ਲਈ ਗੁਪਤ-ਸ਼ਬਦ ਦੀ ਮਿਆਦ ਪੁਗਾ ਦਿਉ (ਸਿਰਫ ਰੂਟ)"
    """)
    po.additem("""\
#: passwd.c:171
msgid "force operation"
msgstr "ਧੱਕੇ ਨਾਲ ਕਾਰਵਾਈ ਕਰੋ"
    """)
    po.additem("""\
#: passwd.c:173
msgid "maximum password lifetime (root only)"
msgstr "ਗੁਪਤ-ਸ਼ਬਦ ਦੀ ਵੱਧ ਤੋਂ ਵੱਧ ਮਿਆਦ (ਸਿਰਫ ਰੂਟ)"
    """)
    po.additem("""\
#: passwd.c:175
msgid "minimum password lifetime (root only)"
msgstr "ਗੁਪਤ-ਸ਼ਬਦ ਦੀ ਘੱਟ ਤੋਂ ਘੱਟ ਮਿਆਦ (ਸਿਰਫ ਰੂਟ)"
    """)
    po.additem("""\
#: passwd.c:177
msgid ""
"number of days warning users receives before password expiration (root only)"
msgstr ""
"ਗੁਪਤ-ਸ਼ਬਦ ਦੀ ਮਿਆਦ ਪੁੱਗਣ (ਸਿਰਫ ਰੂਟ) ਤੋਂ ਪਹਿਲਾਂ ਯੂਜ਼ਰਾਂ ਨੂੰ ਚੇਤਾਵਨੀ ਦੇਣ ਲਈ "
"ਦਿਨਾਂ ਦੀ ਗਿਣਤੀ"
    """)
    po.additem("""\
#: passwd.c:180
msgid ""
"number of days after password expiration when an account becomes disabled "
"(root only)"
msgstr ""
"ਗੁਪਤ-ਸ਼ਬਦ ਦੀ ਮਿਆਦ ਪੁੱਗਣ ਤੋਂ ਬਾਅਦ ਖਾਤਾ ਬੰਦ ਕਰਨ (ਸਿਰਫ ਰੂਟ) ਦਿਨਾਂ ਦੀ ਗਿਣਤੀ"
    """)
    po.additem("""\
#: passwd.c:183
msgid "report password status on the named account (root only)"
msgstr "ਦਿੱਤੇ ਗਏ ਨਾਂ ਵਾਲੇ ਖਾਤੇ (ਸਿਰਫ ਰੂਟ) ਲਈ ਗੁਪਤ-ਸ਼ਬਦ ਦੀ ਹਾਲਤ ਦੀ ਸੂਚਨਾ ਦਿਉ"
    """)
    po.additem("""\
#: passwd.c:186
msgid "read new tokens from stdin (root only)"
msgstr "stdin (ਸਿਰਫ ਰੂਟ) ਤੋਂ ਨਵੇਂ ਟੋਕਨ ਪੜ੍ਹੋ"
    """)
    po.additem("""\
#: passwd.c:193
msgid "[OPTION...] <accountName>"
msgstr "[ਚੋਣ...] <accountName>"
    """)
    po.additem("""\
#: passwd.c:257
#, c-format
msgid "%s: Only one of -l, -u, -d, -S may be specified.\\n"
msgstr "%s: -l, -u, -d, -S ਵਿੱਚੋਂ ਸਿਰਫ ਇੱਕ ਦਰਸਾਇਆ ਜਾ ਸਕਦਾ।\\n"
    """)
    po.additem("""\
#: passwd.c:266
#, c-format
msgid "%s: Cannot mix one of -l, -u, -d, -S and one of -i, -n, -w, -x.\\n"
msgstr ""
"%s: -l, -u, -d, -S ਵਿੱਚੋਂ ਇੱਕ ਅਤੇ -i, -n, -w, -x ਵਿੱਚੋਂ ਇੱਕ ਨੂੰ ਮਿਸ਼ਰਤ ਨਹੀਂ "
"ਕਰ ਸਕਦਾ।\\n"
    """)
    po.additem("""\
#: passwd.c:282
#, c-format
msgid "Only root can do that.\\n"
msgstr "ਸਿਰਫ ਰੂਟ ਹੀ ਉਹ ਕਰ ਸਕਦਾ ਹੈ।\\n"
    """)
    po.additem("""\
#: passwd.c:295
#, c-format
msgid "%s: Only root can specify a user name.\\n"
msgstr "%s: ਸਿਰਫ ਰੂਟ ਹੀ ਇੱਕ ਯੂਜ਼ਰ ਨਾਂ ਦੇ ਸਕਦਾ ਹੈ।\\n"
    """)
    po.additem("""\
#: passwd.c:304
#, c-format
msgid "%s: The user name supplied is too long.\\n"
msgstr "%s: ਦਿੱਤਾ ਗਿਆ ਯੂਜ਼ਰ ਨਾਂ ਬਹੁਤ ਲੰਮਾ ਹੈ\\n"
    """)
    po.additem("""\
#: passwd.c:314
#, c-format
msgid "%s: Only one user name may be specified.\\n"
msgstr "%s: ਸਿਰਫ਼ ਇੱਕ ਯੂਜ਼ਰ ਨਾਂ ਦਿੱਤਾ ਜਾ ਸਕਦਾ ਹੈ\\n"
    """)
    po.additem("""\
#: passwd.c:324
#, c-format
msgid "%s: This option requires a user name.\\n"
msgstr "%s: ਇਸ ਚੋਣ ਨੂੰ ਇੱਕ ਯੂਜ਼ਰ ਨਾਂ ਲੋੜੀਂਦਾ ਹੈ।\\n"
    """)
    po.additem("""\
#: passwd.c:335
#, c-format
msgid "%s: Can not identify you!\\n"
msgstr "%s: ਤੁਹਾਨੂੰ ਪਛਾਣ ਨਹੀਂ ਸਕਦਾ!\\n"
    """)
    po.additem("""\
#: passwd.c:344 passwd.c:379
#, c-format
msgid "%s: Unknown user name '%s'.\\n"
msgstr "%s: ਅਣਪਛਾਤਾ ਯੂਜ਼ਰ ਨਾਂ '%s'\\n"
    """)
    po.additem("""\
#: passwd.c:388
#, c-format
msgid "%s: SELinux denying access due to security policy.\\n"
msgstr "%s: ਸੁਰੱਖਿਆ ਨੀਤੀ ਦੇ ਕਰ ਕੇ SELinux ਦਖਲ ਤੋਂ ਇਨਕਾਰੀ ਹੈ।\\n"
    """)
    po.additem("""\
#: passwd.c:398
#, c-format
msgid "Locking password for user %s.\\n"
msgstr "ਯੂਜ਼ਰ %s ਲਈ ਗੁਪਤ-ਸ਼ਬਦ ਤਾਲਾਬੰਦ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ।\\n"
    """)
    po.additem("""\
#: passwd.c:402 passwd.c:414 passwd.c:429 passwd.c:440 passwd.c:458
msgid "Success"
msgstr "ਸਫ਼ਲਤਾ"
    """)
    po.additem("""\
#: passwd.c:410
#, c-format
msgid "Unlocking password for user %s.\\n"
msgstr "ਯੂਜ਼ਰ %s ਲਈ ਤਾਲ੍ਹਾ ਖੋਲ੍ਹਿਆ ਜਾ ਰਿਹਾ\\n"
    """)
    po.additem("""\
#: passwd.c:425
#, c-format
msgid "Expiring password for user %s.\\n"
msgstr "ਯੂਜ਼ਰ %s ਲਈ ਗੁਪਤ-ਸ਼ਬਦ ਮਿਆਦ ਪੁਗਾ ਰਿਹਾ\\n"
    """)
    po.additem("""\
#: passwd.c:437
#, c-format
msgid "Removing password for user %s.\\n"
msgstr "ਯੂਜ਼ਰ %s ਲਈ ਗੁਪਤ-ਸ਼ਬਦ ਹਟਾਇਆ ਜਾ ਰਿਹਾ ਹੈ।\\n"
    """)
    po.additem("""\
#: passwd.c:455
#, c-format
msgid "Adjusting aging data for user %s.\\n"
msgstr "%s ਯੂਜ਼ਰ ਲਈ ਮਿਆਦ ਡਾਟਾ ਠੀਕ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ।\\n"
    """)
    po.additem("""\
#: passwd.c:471
#, c-format
msgid "Changing password for user %s.\\n"
msgstr "%s ਲਈ ਗੁਪਤ-ਸ਼ਬਦ ਬਦਲਿਆ ਜਾ ਰਿਹਾ ਹੈ।\\n"
    """)
    po.additem("""\
#: passwd.c:489
#, c-format
msgid "%s: error reading from stdin: %s\\n"
msgstr "%s: stdin ਤੋਂ ਪੜ੍ਹਨ ਵਿੱਚ ਅਸਫ਼ਲ: %s\\n"
    """)
    po.additem("""\
#: passwd.c:515
#, c-format
msgid "%s: unable to start pam: %s\\n"
msgstr "%s: ਪੈਮ ਸੁਰੂ ਕਰਨ ਤੋਂ ਅਸਮਰੱਥ: %s\\n"
    """)
    po.additem("""\
#: passwd.c:528
#, c-format
msgid "%s: unable to set tty for pam: %s\\n"
msgstr "%s: pam ਲਈ tty ਸੈੱਟ ਕਰਨ ਤੋਂ ਅਸਮਰੱਥ: %s\\n"
    """)
    po.additem("""\
#: passwd.c:539
#, c-format
msgid "%s: unable to set failure delay: %s\\n"
msgstr "%s: ਅਸਫਲਤਾ ਅੰਤਰਾਲ ਸੈੱਟ ਕਰਨ ਤੋਂ ਅਸਮਰੱਥ: %s\\n"
    """)
    po.additem("""\
#: passwd.c:553
#, c-format
msgid "%s: expired authentication tokens updated successfully.\\n"
msgstr "%s ਮਿਆਦ ਪੁੱਗੇ ਪਰਮਾਣਿਕਤਾ ਸਫਲਤਾਪੂਰਵਕ ਟੋਕਨ ਅੱਪਡੇਟ ਕੀਤੇ ਗਏ।\\n"
    """)
    po.additem("""\
#: passwd.c:556
#, c-format
msgid "%s: all authentication tokens updated successfully.\\n"
msgstr "%s: ਸਭ ਪਰਮਾਣਿਕਤਾ ਟੋਕਨ ਸਫਲਤਾਪੂਰਵਕ ਅੱਪਡੇਟ ਕੀਤੇ ਗਏ।\\n"
    """)
    pofiles.add(po)
    po = t25l.PoFile.from_scratch("ta")
    po.additem("""\
#: passwd.c:162
msgid "lock the password for the named account (root only)"
msgstr "பெயரிடப்பட்ட கணக்குக்கான கடவுச்சொல்லை பூட்டு (ரூட் மட்டும்)"
    """)
    po.additem("""\
#: passwd.c:165
msgid "unlock the password for the named account (root only)"
msgstr "பெயரிடப்பட்ட கணக்குக்கான கடவுச்சொல்லை பூட்டுநீக்கு (ரூட் மட்டும்)"
    """)
    po.additem("""\
#: passwd.c:168
msgid "expire the password for the named account (root only)"
msgstr "பெயரிடப்பட்ட கணக்குக்கான கடவுச்சொல்லை காலாவதியாக்கு (ரூட் மட்டும்)"
    """)
    po.additem("""\
#: passwd.c:177
msgid ""
"number of days warning users receives before password expiration (root only)"
msgstr ""
"கடவுச்சொல் முடிவுறுவதற்கு முன் பயனர்கள் பெறும் எச்சரிக்கை நாட்களின் "
"எண்ணிக்கை (ரூட் மட்டும்)"
    """)
    po.additem("""\
#: passwd.c:180
msgid ""
"number of days after password expiration when an account becomes disabled "
"(root only)"
msgstr ""
"கடவுச்சொல் முடிந்த பின் கணக்கு செயல்நீக்கப்படும் நாட்களின் எண்ணிக்கை (ரூட் "
"மட்டும்)"
    """)
    po.additem("""\
#: passwd.c:266
#, c-format
msgid "%s: Cannot mix one of -l, -u, -d, -S and one of -i, -n, -w, -x.\\n"
msgstr ""
"%s: -l, -u, -d, -S இல் ஒன்று மற்றும்  -i, -n, -w, -x இல் ஒன்றை கலக்க "
"முடியாது.\\n"
    """)
    po.additem("""\
#: passwd.c:388
#, c-format
msgid "%s: SELinux denying access due to security policy.\\n"
msgstr "%s: பாதுகாப்பு கொள்கையின் காரணமாக SELinux அணுகலை மறுக்கிறது.\\n"
    """)
    po.additem("""\
#: passwd.c:425
#, c-format
msgid "Expiring password for user %s.\\n"
msgstr "பயனர் %s க்கான கடவுச்சொல்லை காலாவதியாக்குகிறது.\\n"
    """)
    pofiles.add(po)
    return pofiles
