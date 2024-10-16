module m_control( input [19:0] instruccion, reg [31:0] salidaOperacion);

reg [1:0] MC;
reg [4:0] OP_A;
reg [4:0] OP_B;
reg [3:0] ALUC;
reg [4:0] MEMB;


reg [4:0] direccionEscrituraMemA;
wire [31:0] primerSalidaMemA;
wire [31:0] segundaSalidaMemA;
reg [31:0] datosMemA;


wire [31:0] resultadoAlu;
wire zeroflag;

// wire [31:0] salidaMemB;

m_registros registros (.WE(MC[1]), .primerDireccionLectura(OP_A), .segundaDireccionLectura(OP_B), .direccionEscritura(direccionEscrituraMemA),
	.primerSalida(primerSalidaMemA), .segundaSalida(segundaSalidaMemA), .datos(datosMemA));

m_alu alu (.primerOperando(primerSalidaMemA), .segundoOperando(segundaSalidaMemA), .selector(ALUC), .resultado(resultadoAlu), .zeroflag(zeroflag));

m_memoria memoriaB (.direccion(MEMB), .datos(resultadoAlu), .we(MC[0]), .salida(salidaOperacion));

always @* begin 
	MC = instruccion[19:18];
	OP_A = instruccion[17:13];
	ALUC = instruccion[12:10];
	OP_B = instruccion[9:5];
	MEMB = instruccion[4:0];
end




endmodule
