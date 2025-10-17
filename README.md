# ScaleIQTest
Testing on the ScaleIQ Artificial Intelligence Agent
# 🔹 Flujo QA – Casos de prueba funcionales y bugs

## 1️⃣ Issue funcional sin errores
1. To Test → In Test  
2. Ejecutar la prueba.  
3. ✅ Si pasa sin errores → mover a Passed.  
4. Cuando se documenta → Closed.

---

## 2️⃣ Issue funcional con error detectado
1. To Test → In Test  
2. ❌ Si se detecta un error → mover la issue funcional a Bug Detected.  
   - Anotar brevemente el error y evidencia en la descripción o comentario.

3. Crear **issue técnica tipo Bug**:
   - Completar título, descripción, pasos, resultado esperado/obtenido, evidencia, entorno.  
   - Incluir link a la issue funcional: `Relacionado con: #<nº-issue-funcional>`.  
   - Asignar al dev y mover a Bug Reported.

4. En la **issue funcional**, comentar:
```markdown
🚨 Bug reportado: #<nº-issue-bug>
Estado: movida a Bug Reported / pendiente fix dev
3️⃣ Columna / estado de las issues
Columna	Qué contiene
To Test	Casos listos para ejecutar
In Test	Casos en ejecución
Bug Detected	Issue funcional que falló, sin issue Bug todavía
Bug Reported	Issue Bug creada y reportada al dev
Retest	Issue funcional lista para re-ejecución tras fix
Passed	Casos que pasaron correctamente
Failed	Casos que siguen fallando después del fix
Closed	Casos terminados o archivados
4️⃣ Linkeo entre issue funcional y bug

En la issue Bug:

Relacionado con: #<nº-issue-funcional>


En la issue funcional:

Bug reportado: #<nº-issue-bug>


Esto permite ver la relación directa y mantener el seguimiento claro.
┌───────────┐
│  To Test  │
└─────┬─────┘
      │
      ▼
┌───────────┐
│  In Test  │
└─────┬─────┘
      │
      ├───────────────▶ ✅ Sin errores
      │                     │
      │                     ▼
      │             ┌────────────┐
      │             │   Passed   │
      │             └──────┬─────┘
      │                    ▼
      │             ┌────────────┐
      │             │   Closed   │
      │             └────────────┘
      │
      └───────────────▶ ❌ Error detectado
                        │
                        ▼
                ┌────────────────┐
                │  Bug Detected  │ ← Issue funcional anotada
                └──────┬─────────┘
                       │
                       ▼
                ┌────────────────┐
                │  Bug Reported  │ ← Issue Bug creada
                └──────┬─────────┘
                       │ (Developer corrige y cierra bug)
                       ▼
                ┌────────────────┐
                │     Retest     │ ← QA re-testea la issue funcional
                └──────┬─────────┘
                       │
           ┌───────────┼───────────┐
           ▼                       ▼
     ┌────────────┐         ┌────────────┐
     │   Passed   │         │   Failed   │
     └──────┬─────┘         └──────┬─────┘
            ▼                      ▼
     ┌────────────┐         ┌────────────┐
     │   Closed   │         │   Closed   │
     └────────────┘         └────────────┘

