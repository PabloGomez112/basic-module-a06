module m_registros(
		      input [4:0] primerDireccionLectura,
		      input [4:0] segundaDireccionLectura,
		      input [4:0] direccionEscritura,
		      input WE, 
		      input [31:0] datos,
		      output reg [31:0] primerSalida,
		      output reg [31:0] segundaSalida);

reg [31:0] memoria [31:0];

initial begin
$display("Cargando datos"); 
$readmemh("datos", memoria);
end



always @* begin
	if (WE) begin
		memoria[direccionEscritura] = datos;
	end

	else begin 
		assign primerSalida = memoria[primerDireccionLectura];
		assign segundaSalida = memoria[segundaDireccionLectura];
		
		$display("primerSalida: %b", primerSalida);
		$display("segundaSalida: %b", segundaSalida);	
	end
end

endmodule