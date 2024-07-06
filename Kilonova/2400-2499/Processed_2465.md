# Input data

Each test contains multiple test cases. The first line from `stdin` will contain the number of test cases $t$.

Each test case contains a matrix of $9 \times 9$ lowercase letters from the English alphabet.

# Output data

For each test case, print in `stdout` "YES" or "NO".

# Constraints and clarifications

* $1 \leq t \leq 10^4$;
* For tests worth $50$ points, $t=1$.

# Example 1

`stdin`
```
1
sbcdefghi
accdefghi
abrdefghi
abciefghi
abcdsfghi
abcdeoghi
abcdefahi
abcdefgri
abcdefghe
```

`stdout`
```
YES
```

# Example 2

`stdin`
```
1
catavencu
pristanda
tipatescu
suntperso
najedinco
mediaoscr
isoarepie
rdutadeil
caragiale
```

`stdout`
```
NO
```

## Explanation

Catavencu, Pristanda, Tipatescu are characters from the comedy "O scrisoare pierduta" by I. L. Caragiale.

# Example 3

`stdin`
```
8
esisrisce
creoaiarr
iaaorcirs
crooicses
icoossisc
rseosirrc
sriscsror
xeqrojsci
oegeersos
roisarisp
aiicscssr
rsrrcrras
iccirssri
caysccosl
ooroejgaa
icoaerkrc
cjwreeere
rrsessosc
rsreirzce
oersrcaro
oaecssaae
ivrraoqss
dezasosse
sooiiasss
sororaarc
scrsrsrss
ssrcecrls
carsascro
scscsiici
rybrrsrrs
rsreeosic
ohrsiaora
ssosaveii
eciawcsss
eerseorae
scesrirrg
sreoeiari
ecshwsiis
ierarrcsc
stoissrsc
rdocstsia
essseoees
soiaosaor
asaiiorra
orcaicrie
orrorasos
ecceasrcc
osrirsris
scccricra
iriascrea
earorsoce
asarraorr
rrisierrr
ercosisar
ororeairi
aroaguoor
caroorssa
eceoorsca
asccrsoio
reoasomrr
esrreairr
srsorirrc
scrisoare
irebrcssz
cahoiaopc
ascaoroso
sarriross
scrisoare
oasanzase
iaricssrs
iewreoioo
irrasfawr
```

`stdout`
```
YES
YES
YES
NO
YES
YES
YES
YES
```
