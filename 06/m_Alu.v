module m_alu(input [31:0] primerOperando,
			 input [31:0] segundoOperando,
			 input [3:0] selector,
			 output reg [31:0] resultado,
			 output reg zeroflag);

	localparam AND = 4'b0000;
	localparam OR = 4'b0001;
	localparam add = 4'b0010;
	localparam subtract = 4'b0110;
	localparam slt = 4'b0111;
	localparam NOR = 4'b1100;
	localparam ZERO = 0;


always @* begin
	case (selector)  
			AND: resultado = primerOperando & segundoOperando; // Compuerta AND
			OR: resultado = primerOperando | segundoOperando;
			add: resultado = primerOperando + segundoOperando;
			subtract: resultado = primerOperando - segundoOperando;
			slt: resultado = primerOperando < segundoOperando ? 1'b1 : 1'b0;
			NOR: resultado = !(primerOperando | segundoOperando);
			default: resultado = ZERO;
		endcase
		
		zeroflag = (resultado == ZERO ? 1'b1 : 1'b0);
end

endmodule