Python Text-to-Speech Converter (Mac/Windows)
=============================================

A simple, high-quality Text-to-Speech tool using Microsoft Edge's Neural Voice technology. This tool allows you to convert text files (story.txt) into audio files (audiobook.mp3) with precise control over speed, pitch, and voice selection.

📦 Installation
---------------

Before running the script, make sure you have the required library installed in your environment.

Bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install edge-tts   `

🚀 How to Run
-------------

1.  Place your text in a file named story.txt.
    
2.  Run the script using Python:
    

Bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python mac_speech.py   `

1.  The audio will be saved as audiobook.mp3 and will play automatically.
    

⚙️ Settings
-----------

You can adjust the following variables inside the Python script (mac\_speech.py) to customize the output.

### 1\. Speed (Rate)

Controls how fast the voice speaks.

*   **Format:** "+percentage%" or "-percentage%"
    
*   **Default:** "+0%"
    

**SettingEffect**RATE = "-50%"Very SlowRATE = "-10%"Slightly SlowRATE = "+0%"Normal SpeedRATE = "+10%"Slightly FastRATE = "+50%"Very Fast

### 2\. Pitch

Controls the tone of the voice.

*   **Format:** "+Hz" or "-Hz"
    
*   **Default:** "+0Hz"
    

**SettingEffect**PITCH = "-10Hz"Very Deep VoicePITCH = "-2Hz"Slightly DeeperPITCH = "+0Hz"Normal TonePITCH = "+2Hz"Slightly HigherPITCH = "+10Hz"Very High (Chipmunk-like)

🗣️ Available Voices
--------------------

You can change the VOICE variable to any of the IDs below.

### 🇺🇸 English (US)

*   en-US-AriaNeural (Female) **\[Recommended\]**
    
*   en-US-GuyNeural (Male) **\[Recommended\]**
    
*   en-US-JennyNeural (Female)
    
*   en-US-MichelleNeural (Female)
    
*   en-US-RogerNeural (Male)
    

### 🇮🇳 English (India)

*   en-IN-NeerjaNeural (Female)
    
*   en-IN-PrabhatNeural (Male)
    

### 🇬🇧 English (UK)

*   en-GB-SoniaNeural (Female)
    
*   en-GB-RyanNeural (Male)
    

### 🇦🇺 English (Australia)

*   en-AU-NatashaNeural (Female)
    
*   en-AU-WilliamNeural (Male)
    

### Other Languages

*   **Hindi:** hi-IN-SwaraNeural (Female) / hi-IN-MadhurNeural (Male)
    
*   **French:** fr-FR-DeniseNeural (Female) / fr-FR-HenriNeural (Male)
    
*   **Spanish:** es-ES-ElviraNeural (Female) / es-ES-AlvaroNeural (Male)
    

🔍 How to find more voices?
---------------------------

To see a list of **every single voice** available on your system, run this command in your terminal:

Bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   edge-tts --list-voices   `