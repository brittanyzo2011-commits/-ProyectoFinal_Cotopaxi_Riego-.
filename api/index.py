from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        html_content = """
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>Evaluación Impacto Riego Cotopaxi</title>
            <style>
                body { font-family: 'Segoe UI', sans-serif; margin: 0; padding: 40px; background-color: #f8fafc; color: #1e293b; }
                .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
                h1 { color: #0284c7; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; }
                .badge { background: #0284c7; color: white; padding: 4px 12px; border-radius: 12px; font-size: 14px; }
                .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-top: 20px; }
                .card { background: #f0f9ff; border: 1px solid #bae6fd; padding: 15px; border-radius: 8px; text-align: center; }
                .metric { font-size: 20px; font-weight: bold; color: #0369a1; }
            </style>
        </head>
        <body>
            <div class="container">
                <span class="badge">PROYECTO INTEGRADOR FINAL</span>
                <h1>EVALUACIÓN DE IMPACTO DE POLÍTICA PÚBLICA</h1>
                <p><strong>Programa de Riego Tecnificado y Conservación de Páramos en Cotopaxi</strong></p>
                <hr>
                <h2>Resultados Econométricos (Modelo PSM)</h2>
                <div class="grid">
                    <div class="card">
                        <div>Impacto Ingreso</div>
                        <div class="metric">+$ 130.50 USD</div>
                        <small>+31.6% (p &lt; 0.001)</small>
                    </div>
                    <div class="card">
                        <div>Rendimiento</div>
                        <div class="metric">+ 3.43 Ton/Ha</div>
                        <small>+40.7% (p &lt; 0.001)</small>
                    </div>
                    <div class="card">
                        <div>Retorno B/C</div>
                        <div class="metric">1.84</div>
                        <small>Viabilidad Alta</small>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html_content.encode('utf-8'))
