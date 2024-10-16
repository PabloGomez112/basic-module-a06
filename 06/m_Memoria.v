module m_memoria(input [4:0] direccion, 
				 input [31:0] datos, 
				 input we, 
				 output reg [31:0]salida);

reg [31:0] memoriaRam [31:0]; 

always @* begin
	if (we) begin 
	memoriaRam[direccion] = datos;
	end

	else begin
		salida = memoriaRam[direccion];
	end
end

endmodule