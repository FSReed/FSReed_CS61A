(begin
  (define (f x total)
    (if (< (* x x) 50)
      (f (+ x 1) (+ total x))
      total))
  (f 1 0))

(define (sum-while starting-x while-condition add-to-total update-x)
  `(begin
    (define (f x total)
      (if ,while-condition
        (f ,update-x (+ total ,add-to-total))
        total))
    (f ,starting-x 0)))