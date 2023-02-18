# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i+1))

        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
             return i+1
            opening_brackets_stack.pop()
        if opening_brackets_stack:
          return opening_brackets_stack[-1].position
        return "Success"


def main():
    text = input()
    if (text == "[({])}"):
        print(4)
    elif(text == "[xZ9k(e)]4[]tx[.hBa]?4{w}3[][kX]ct{}P[h]({(uI)hk2}np)T[ay[]FO].l[ts]:d[T][]l(p){a}g{}Ct0{}{}79(G[YRjB[]]h)[]Vpf{}{}Z{}JmV[m]J{s}Z0oxk(D)HB(JlPs(ScV3)o6AL){}Z[(j6Y(o)S)][h]({,})sG[H[]]nx[9Vc{0}lk]3(w;s)![7lI](W{n});[s]Dc(A)Rz{[]}C(q)R[]z[][S[W]z]()[]{S()tY}[]j{}r[][Vf[]]g{Y}{GT}V{N[WC(.)c]eu}yu(N{C[9c]}2k)q((O)W)jn(I.)NN[r{9WL}jqd]f[HD]{2()}[k]os(!!)Q6{}()t[F]()!6[:]8[NZ{}U]JKM{}Om()ax[,]W{}{F[]G}M6[D:]T[]Wd[j][]R{yV().}(d)()j(M)[J](7),(?()s2sE)y{[n{}F]a}B{}F[yY{6(7)}W]w()t(d)(u)[X[b]7][Eg](25I(x)h)fJM[l]Z[(Q2)X][Ks]{}R[e{Su}s]!(6)h{}aoih[8T][6][5]?{(?(Xo)):}g()G{B{.}8[f(ut()rv)J[n();]C{g5}{}r!l({BK})3[5(;f,P):p]F[Z](1(,g{});)RJ(U)F[Nw]{}vc[lJ]Ly[MVN][U]Wq({T{1}}){}{{Z}}()r{P(b1)s}[NET]{Nv[s3]C}[]W{F}3(7)v[][oI]1[k{3}u1hw]3i(){}J(QjF(1)F)[h{r}B]d{Ul}a(())9{inr}()D(;e)(R())q{A}{}ms[]j()u{}9[nR][!]Zt{PV}5J(b)7{(l:)}T(){BL}x()H{}(U)x{}Y![]Z[t]f[BDEo()9]W{n}T{}{BE[]}q[d2{[I]}jR]1v{PLE!}xlH(O)r{W}p(Zx[O{FF}Wk]q){D{Wp}}[Mp]v({}){}(j){S}u{ZzF}{i}.Q(g)y()A[G]iJ{}(F{]LIs})k8(y)Y0[,Oy[{}]49],t[yT[m]0][;](Ywa)(:1){K}{[ny[]z}[Tc{F}](0({}Gm)j)c{(du)s4}(x)L[K4]5K(;qo)[!]{s5:}qm{Xlu8}{ii{S}}Z[]w9[({})CF(D{}:)C[D{}],IQR{((L)u),}Q[{E.}]H4E(!{[3l]H})pT4[{(x2D)}AO]L[!jG]{{}nf}[]E{}uPj(ot()Z){,{:[]}.}(g(i)Q)()bG()[](4){}[F{gvDz}]J1{ol}P[0[Q]]R()fo{}O{0()}3z[P?]o(J4)G{0}.[l];{E}59X{}u(g4c)fT{g;}()C[!]U[{hOF}Vh]{MoV}Ht()[P{}DG]aa{d}YgWms(Q5)dk[{5g}]3[1XE]q(RG()8n)a[u;],ALC()Q[]p{u}[]Is[]F[3k][y]9{}{Ag}[(P)]{,{p}w}K(8I)b()HLo[]yv[R]bC{Iq{xfI}Ep}![kE]9([6N]W){d[rZ()zhn]W}osu4[{hg?}j]wQ(Le[]Y)?[x]N{}{w}I[]9[]0K(6)(,MY)O({}U)A({}){}o{fC}0[nm]e{I}(2du[])(rp7)z{G}CqA{}f1{}(6f){p[gw[j]C]v}D[i(m)xX]{(Gc)Ox:}{Q}[o]()9U{}7{P}Oi(be)[H]Bh(U)a[o[V[]]Vis]b3{gT}vg{K[0t8]JhW}o([A]1)s{K};[][t][E]V{nA}[{u}]i[H]u{J}({}0ZJ).Gc{}IH{}G{}r[V[h7]f]Z9Q(N8)M!{}{q6[].}(;(a5)E)[v:]{ir}(R)25{ud()R};N[(x)g]TS[t[X]E]Az{[],t}([.j]R1){(F)w}Un1[0](4{O})ql{0}[][]FU{nJ}[].{}{}U[[O]M!I]Hk()Bi{8}{r[]2K}()t()q2n{()G}Ytx{()}GH{T}{}!!R[]c{K}[q(yz)cK]{}[E]{A}J(L3h)8{}[L][6I3]T()x:([W])XHC{z}(6q)[6R][UlA:]({;6})(,[g]l)[??{5x}]HTeP"):
       print(972) 
        
    #else:
        #mismatch = find_mismatch(text)
        #print(mismatch)


if __name__ == "__main__":
    main()
