`timescale 1ns/1ns

module tb_control();

reg [19:0] instruccion;
wire [31:0] resultado;
reg [19:0] memoriaInstrucciones [31:0];

reg [4:0] actualPos; 



m_control control(.instruccion(instruccion), .salidaOperacion(resultado));

initial begin 
	
	$readmemb("instrucciones.txt", memoriaInstrucciones);

	for(actualPos = 5'b0; actualPos < 5'd31; actualPos = actualPos + 1) begin
		#100;
		instruccion = memoriaInstrucciones[actualPos];
		
	end
	$stop;
end


endmodule;