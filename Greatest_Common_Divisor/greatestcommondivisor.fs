open System

let token = (Console.In.ReadLine()).Split [|' '|]
let a = int(token.[0])
let b = int(token.[1])

let rec gcd (m,n) =
    match (m,n) with
        | (0,n) -> n
        | (m,n) -> gcd(n % m,m)

printfn "%A" (gcd (a,b))
