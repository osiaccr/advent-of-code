import Control.Monad
import Data.List.Extra
import Data.Maybe
import qualified Data.Char as C
import qualified Data.Map as Map
import qualified Data.Set as Set

------
iread :: String -> Int
iread = read

do2 f g x = (f x, g x)

answer :: (Show a) => (String -> a) -> IO ()
answer f = interact $ (++"\n") . show . f

ord0 c = C.ord c - C.ord 'a'
chr0 i = C.chr (i + C.ord 'a')
incletter c i = chr0 ((ord0 c + i) `mod` 26)

splitOn1 a b = fromJust $ stripInfix a b
rsplitOn1 a b = fromJust $ stripInfixEnd a b

-- pull out every part of a String that can be read in
-- for some Read a and ignore the rest
readOut :: Read a => String -> [a]
readOut "" = []
readOut s = case reads s of
  [] -> readOut $ tail s
  [(x, s')] -> x : readOut s'
  _ -> error "ambiguous parse"
ireadOut :: String -> [Int]
ireadOut = readOut

--------


stripGarbage ('>':l) = (0,l)
stripGarbage ('!':_:l) = stripGarbage l
stripGarbage (_:l) = let (n, l') = stripGarbage l in (n+1, l')

cleanGarbage ('<':l) = let (n, l') = stripGarbage l in n+cleanGarbage l'
cleanGarbage (x:l) = cleanGarbage l
cleanGarbage [] = 0


main = answer $ cleanGarbage . filter (/= '\n')
