(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement

(define (zip pairs)
  'replace-this-line)


;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  (define (enumerate-helper s order) 
    (if (null? s) nil 
      (cons (cons order (cons (car s) nil)) (enumerate-helper (cdr s) (+ order 1)))
      )
  )
  (enumerate-helper s 0)
  )
  ; END PROBLEM 15

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to COMP and return
;; the merged lists.
(define (merge comp list1 list2)
  ; BEGIN PROBLEM 16
  (cond
    ((null? list1) list2)
    ((null? list2) list1)
    (else
      (if (comp (car list1) (car list2)) 
        (cons (car list1) (merge comp (cdr list1) list2))
        (cons (car list2) (merge comp list1 (cdr list2)))
      )
    )
  )
)
  ; END PROBLEM 16


(merge < '(1 5 7 9) '(4 8 10))
; expect (1 4 5 7 8 9 10)
(merge > '(9 7 5 1) '(10 8 4 3))
; expect (10 9 8 7 5 4 3 1)

;; Problem 17

(define (nondecreaselist s)
    ; BEGIN PROBLEM 17
  (if (null? s) nil
    (begin 
      (define (helper prev_sequence sequece_now prev_value)
        (if (or (null? sequece_now) (< (car sequece_now) prev_value))
          (cons prev_sequence sequece_now)
          (helper (append prev_sequence (cons (car sequece_now) nil)) (cdr sequece_now) (car sequece_now))
        )
      )
      (define result_pair (helper nil s (car s)))
      ; (print result_pair)
      ; (print (cdr result_pair))
      (define first_sequence (car result_pair))
      (define rest_sequence (cdr result_pair))
      ; (print first_sequence)
      ; (print rest_sequence)
      (if (null? rest_sequence) 
        (cons first_sequence nil)
        (append (cons first_sequence nil) (nondecreaselist rest_sequence))
      ) 
    )
  )
)
    ; END PROBLEM 17
;; Problem EC
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM EC
         'replace-this-line
         ; END PROBLEM EC
         )
        ((quoted? expr)
         ; BEGIN PROBLEM EC
         'replace-this-line
         ; END PROBLEM EC
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM EC
           'replace-this-line
           ; END PROBLEM EC
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM EC
           'replace-this-line
           ; END PROBLEM EC
           ))
        (else
         ; BEGIN PROBLEM EC
         'replace-this-line
         ; END PROBLEM EC
         )))