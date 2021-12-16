open System

let m = int(Console.In.ReadLine())
let n = int(Console.In.ReadLine())
let t = int(Console.In.ReadLine())

let rec animalcount ( rate:int, t:int, (acc,birth,first)) =
    match t with
        | 0 -> acc+birth+first
        | t -> animalcount (rate, t-1, (acc+first, (acc+first)*rate,birth))

printfn "%A" (animalcount ( m, t, (n, 0 ,0)))
