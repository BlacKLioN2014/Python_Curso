from fpdf import FPDF


# Crear clase PDF personalizada
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Rutina de Entrenamiento y Plan Alimenticio', ln=True, align='C')
        self.ln(10)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, ln=True, fill=True)
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 10, body)
        self.ln()


# Crear PDF
pdf = PDF()
pdf.add_page()

# Rutina de entrenamiento con enlaces de videos
pdf.chapter_title('Rutina Semanal (4 Días)')
routine_text = (
    "Día 1 - Tren Superior (Pecho, Hombros, Tríceps):\n"
    "- Press de Pecho en Máquina - 4x10-12\n  Video: https://youtu.be/xxx12345\n"
    "- Elevaciones Laterales - 3x12-15\n  Video: https://youtu.be/xxx67890\n"
    "- Fondos en Banco - 3x10-12\n  Video: https://youtu.be/xxx54321\n"
    "- Extensiones de Tríceps en Polea Alta - 3x12-15\n  Video: https://youtu.be/xxx13579\n"
    "- Plancha Frontal - 3x30 seg\n  Video: https://youtu.be/xxx24680\n\n"

    "Día 2 - Tren Inferior (Piernas sin impacto lumbar):\n"
    "- Prensa de Piernas - 4x10-12\n  Video: https://youtu.be/yyy12345\n"
    "- Curl de Piernas Acostado - 3x12-15\n  Video: https://youtu.be/yyy67890\n"
    "- Elevaciones de Talones - 4x15-20\n  Video: https://youtu.be/yyy54321\n"
    "- Puente de Glúteos - 3x12-15\n  Video: https://youtu.be/yyy13579\n"
    "- Crunches en Máquina - 3x15-20\n  Video: https://youtu.be/yyy24680\n\n"

    "Día 3 - Espalda y Bíceps (sin carga lumbar):\n"
    "- Jalón al Pecho - 4x10-12\n  Video: https://youtu.be/zzz12345\n"
    "- Remo en Máquina Sentado - 3x10-12\n  Video: https://youtu.be/zzz67890\n"
    "- Curl de Bíceps con Barra Z - 3x12-15\n  Video: https://youtu.be/zzz54321\n"
    "- Curl Martillo - 3x12-15\n  Video: https://youtu.be/zzz13579\n"
    "- Plancha Lateral - 3x30 seg por lado\n  Video: https://youtu.be/zzz24680\n\n"

    "Día 4 - Cardio + Core:\n"
    "- 30 minutos Cardio HIIT\n  Video: https://youtu.be/aaa12345\n"
    "- Circuito de Core (3 rondas): Elevaciones de Pierna, Crunches Bicicleta, Plancha con Toque de Hombro\n  Video: https://youtu.be/aaa67890"
)
pdf.chapter_body(routine_text)

# Planes alimenticios
pdf.chapter_title('Planes Alimenticios')

meal_plans = [
    "Plan 1:\n- Desayuno: Avena con claras de huevo y plátano.\n- Almuerzo: Pollo a la plancha, arroz integral y brócoli.\n- Cena: Pescado con ensalada verde y aguacate.\n- Snack: Yogur griego natural con almendras.",
    "Plan 2:\n- Desayuno: 2 huevos enteros, 3 claras, pan integral, café negro.\n- Almuerzo: Carne magra, quinoa y espárragos.\n- Cena: Pechuga de pollo con calabacitas salteadas.\n- Snack: Batido de proteína con crema de cacahuate.",
    "Plan 3:\n- Desayuno: Smoothie de proteína, avena, chía y fresas.\n- Almuerzo: Salmón con papa cocida y ensalada mixta.\n- Cena: Omelette de claras con espinaca.\n- Snack: Manzana con un puñado de nueces.",
    "Plan 4:\n- Desayuno: Tostadas integrales con aguacate y huevo cocido.\n- Almuerzo: Tacos de pollo en tortillas de maíz con vegetales.\n- Cena: Ensalada de atún con huevo y espinaca.\n- Snack: Gelatina sin azúcar o zanahorias baby."
]

for plan in meal_plans:
    pdf.chapter_body(plan)

# Guardar PDF
pdf_output_path = "Rutina_Y_Plan_Alimenticio.pdf"
pdf.output(pdf_output_path)

print(f"PDF generado exitosamente en: {pdf_output_path}")
