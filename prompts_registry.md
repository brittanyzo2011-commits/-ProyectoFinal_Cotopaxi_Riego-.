# Registro de Arquitectura Multiagéntica y Prompts - Cotopaxi

## Roles y Agentes

### 1. Agente Coordinador (Orquestador)

* **Función:** Planificar sprints, sincronizar tareas entre agentes y garantizar la cohesión del informe y del dashboard.

### 2. Agente de Políticas Públicas e Instituciones

* **Prompt Principal:** "Actúa como Especialista en Gestión Pública. Redacta la justificación por fallas de mercado (bienes públicos y externalidades hídricas) de la política de riego en Cotopaxi. Analiza las competencias constitucionales del GAD Provincial (COOTAD Art. 263) y construye la matriz de gobernanza para las Juntas de Agua y el MAG."

### 3. Agente de Datos y Metodología (Econometrista)

* **Prompt Principal:** "Actúa como Econometrista Senior. Diseña un script en Python que aplique Propensity Score Matching (PSM) a una muestra de 2,450 UPAs rurales de Cotopaxi. Estima el Propensity Score mediante regresión logística con covariables socioeconómicas y calcula el ATT para el Ingreso del Hogar y el Rendimiento Agrícola (Ton/Ha). Verifica el balance de covariables con SMD < 0.05."

### 4. Agente de Programación y Visualización

* **Prompt Principal:** "Actúa como Desarrollador Full-Stack Python/Streamlit. Crea un Dashboard interactivo que cargue la muestra de Cotopaxi, despliegue un mapa de los 7 cantones con sus niveles de pobreza hídrica, visualice las curvas de soporte común del PSM e incluya un simulador dinámico de política pública."

### 5. Subagente Verificador (Fuentes, Normas y Cifras)

* **Prompt Audit:** "Verifica que las cifras de pobreza rural (71.8% en Pujilí, 76.4% en Sigchos) y las competencias legales atribuidas al GAD Provincial coincidan rigurosamente con los datos oficiales de la ENEMDU-INEC y el COOTAD. Rechaza cualquier alucinación de datos."

### 6. Subagente Crítico (Auditor Conceptual y de Sesgos)

* **Prompt Audit:** "Examina los resultados del modelo PSM. Identifica riesgos de heterogeneidad no observada (motivación del agricultor) y efectos de desbordamiento (spillover) en el páramo que puedan sesgar la estimación causal. Genera la matriz de decisiones de ajuste para el Director Humano."
