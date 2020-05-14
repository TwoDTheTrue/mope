.model flat, stdcall
include D:\masm32\include\kernel32.inc
include D:\masm32\include\user32.inc
include module.inc
include longop.inc
includelib D:\masm32\lib\kernel32.lib
includelib D:\masm32\lib\user32.lib
option casemap :none
.data
	a db "Факторіал 82" ,0
	a1 db "82! x 82!" ,0
	b1 db " Множення (111..1*111..1)" ,0
	b2 db "Спрощене множення N*32 (111..1*111..1)" ,0
	b3 db "Множення (111..1*11..100..0)" ,0
	text dd 40 dup(?)
	Text1 dd 40 dup(?)
	Test1 dd 40 dup(?)
	Test2 dd 40 dup(?)
	Test3 dd 40 dup(?)
	y dd 13 dup(0)
	f dd 26 dup(0)
	x dd 82
	test1 dd 13 dup(4294967295)
	test1res dd 26 dup(0)
	test2 dd 13 dup(4294967295)
	test31 dd 13 dup(4294967295)
	test32 dd 13 dup(0)
	test3res dd 26 dup(0)
.code	
	main:
	mov dword ptr [y], 1
	@factorial:
	push offset y
    push x
	call Mul_Nx32_LONGOP 
	dec x
	jnz @factorial
	push offset text
	push offset y
	push 408
	call StrHex_MY
    invoke MessageBoxA, 0, ADDR text, ADDR a, 0
    push offset y
	push offset y
	push offset f
	call Mul_NxN_LONGOP
    push offset Text1
	push offset f
	push 816
	call StrHex_MY
    invoke MessageBoxA, 0, ADDR Text1, ADDR a1, 0
    push offset test1
	push offset test1
	push offset test1res
	call Mul_NxN_LONGOP
    push offset Test1
	push offset test1res
	push 836
	call StrHex_MY
    invoke MessageBoxA, 0, ADDR Test1, ADDR b1, 0
    mov dword ptr [test2 + 16] , 0
    push offset test2
	push 4294967295 ; 0FFFFFFFFh
	call Mul_Nx32_LONGOP
    push offset Test2
	push offset test2
	push 160
	call StrHex_MY
    invoke MessageBoxA, 0, ADDR Test2, ADDR b2, 0
    mov [test32 + 19], 192
	push offset test31
	push offset test32
	push offset test3res
	call Mul_NxN_LONGOP
    push offset Test3
	push offset test3res
	push 580
	call StrHex_MY
    invoke MessageBoxA, 0, ADDR Test3, ADDR b3, 0
	invoke ExitProcess,0
end main
