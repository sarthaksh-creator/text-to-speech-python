import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import edge_tts
import asyncio
import threading
import subprocess
import os

class PremiumTTSApp:
    def __init__(self, root, username="Guest", logout_callback=None):
        self.root = root
        self.username = username
        self.logout_callback = logout_callback
        
        self.root.title("🎙️ AI Voice Studio Pro")
        self.root.geometry("1100x750")
        self.root.resizable(True, True)
        self.root.minsize(900, 650)
        
        # Premium Color Palette
        self.colors = {
            'bg': '#0a0e27',
            'bg_gradient': '#1a1f3a',
            'card_bg': '#141b2d',
            'card_hover': '#1a2332',
            'accent_primary': '#6366f1',
            'accent_secondary': '#8b5cf6',
            'accent_glow': '#a78bfa',
            'success': '#10b981',
            'warning': '#f59e0b',
            'danger': '#ef4444',
            'text_primary': '#f1f5f9',
            'text_secondary': '#94a3b8',
            'text_muted': '#64748b',
            'border': '#1e293b',
            'input_bg': '#0f172a',
            'shadow': '#000000'
        }
        
        self.root.configure(bg=self.colors['bg'])
        
        # Voice Database
        self.voices = {
            "🇺🇸 Emma - Natural Female": "en-US-EmmaNeural",
            "🇺🇸 Andrew - Professional Male": "en-US-AndrewNeural",
            "🇺🇸 Jenny - Warm Female": "en-US-JennyNeural",
            "🇺🇸 Guy - Deep Male": "en-US-GuyNeural",
            "🇬🇧 Sonia - British Female": "en-GB-SoniaNeural",
            "🇬🇧 Ryan - British Male": "en-GB-RyanNeural",
            "🇮🇳 Neerja - Indian Female": "en-IN-NeerjaNeural",
            "🇮🇳 Prabhat - Indian Male": "en-IN-PrabhatNeural",
            "🇦🇺 Natasha - Australian Female": "en-AU-NatashaNeural",
            "🇦🇺 William - Australian Male": "en-AU-WilliamNeural"
        }
        
        self.presets = {
            "🎭 Story Narrator": {"voice": "en-US-GuyNeural", "rate": -10, "pitch": -3, "desc": "Deep, engaging storytelling"},
            "👶 Kids Content": {"voice": "en-US-JennyNeural", "rate": -15, "pitch": 8, "desc": "Friendly and cheerful"},
            "😱 Horror/Thriller": {"voice": "en-US-GuyNeural", "rate": -30, "pitch": -10, "desc": "Dark and suspenseful"},
            "📰 News Broadcast": {"voice": "en-US-EricNeural", "rate": 0, "pitch": 0, "desc": "Clear and professional"},
            "🎵 Energetic": {"voice": "en-US-AriaNeural", "rate": 15, "pitch": 5, "desc": "Upbeat and dynamic"},
            "📚 Audiobook": {"voice": "en-US-EmmaNeural", "rate": -5, "pitch": 0, "desc": "Calm and natural"}
        }
        
        self.output_file = "output.mp3"
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main Container
        main = tk.Frame(self.root, bg=self.colors['bg'])
        main.pack(fill='both', expand=True)
        
        # Top Bar (User info + Logout)
        self.create_top_bar(main)
        
        # Content Container
        content_container = tk.Frame(main, bg=self.colors['bg'])
        content_container.pack(fill='both', expand=True, padx=25, pady=(0, 25))
        
        # Hero Header
        self.create_hero_header(content_container)
        
        # Main Content Grid
        content_grid = tk.Frame(content_container, bg=self.colors['bg'])
        content_grid.pack(fill='both', expand=True, pady=(25, 0))
        
        # Left Panel (Text Editor)
        left_panel = tk.Frame(content_grid, bg=self.colors['bg'])
        left_panel.pack(side='left', fill='both', expand=True, padx=(0, 12))
        
        # Right Panel (Controls)
        right_panel = tk.Frame(content_grid, bg=self.colors['bg'], width=380)
        right_panel.pack(side='right', fill='both', padx=(12, 0))
        right_panel.pack_propagate(False)
        
        # Build Sections
        self.create_text_editor_card(left_panel)
        self.create_voice_selector_card(right_panel)
        self.create_presets_card(right_panel)
        self.create_controls_card(right_panel)
        self.create_action_buttons(right_panel)
        
        # Status Bar
        self.create_status_bar(main)
        
    def create_top_bar(self, parent):
        bar = tk.Frame(parent, bg=self.colors['card_bg'], height=60)
        bar.pack(fill='x')
        bar.pack_propagate(False)
        
        # Add subtle top border glow
        glow = tk.Frame(bar, bg=self.colors['accent_glow'], height=2)
        glow.pack(fill='x')
        
        content = tk.Frame(bar, bg=self.colors['card_bg'])
        content.pack(fill='both', expand=True, padx=25, pady=12)
        
        # User info (left)
        user_frame = tk.Frame(content, bg=self.colors['card_bg'])
        user_frame.pack(side='left')
        
        tk.Label(
            user_frame,
            text="👤",
            font=('SF Pro Display', 16),
            bg=self.colors['card_bg'],
            fg=self.colors['text_primary']
        ).pack(side='left', padx=(0, 8))
        
        tk.Label(
            user_frame,
            text=self.username,
            font=('SF Pro Display', 13, 'bold'),
            bg=self.colors['card_bg'],
            fg=self.colors['text_primary']
        ).pack(side='left')
        
        # Logout button (right)
        if self.logout_callback:
            logout_btn = tk.Button(
                content,
                text="🚪 Logout",
                font=('SF Pro Display', 11),
                bg=self.colors['input_bg'],
                fg=self.colors['text_secondary'],
                activebackground=self.colors['danger'],
                activeforeground='white',
                relief='flat',
                bd=0,
                padx=18,
                pady=8,
                cursor='hand2',
                command=self.logout_callback
            )
            logout_btn.pack(side='right')
            
    def create_hero_header(self, parent):
        header = tk.Frame(parent, bg=self.colors['bg'])
        header.pack(fill='x', pady=(15, 0))
        
        # Title with gradient effect simulation
        title_frame = tk.Frame(header, bg=self.colors['bg'])
        title_frame.pack()
        
        tk.Label(
            title_frame,
            text="🎙️",
            font=('SF Pro Display', 42),
            bg=self.colors['bg']
        ).pack(side='left', padx=(0, 12))
        
        text_frame = tk.Frame(title_frame, bg=self.colors['bg'])
        text_frame.pack(side='left')
        
        tk.Label(
            text_frame,
            text="AI Voice Studio",
            font=('SF Pro Display', 32, 'bold'),
            bg=self.colors['bg'],
            fg=self.colors['text_primary']
        ).pack(anchor='w')
        
        tk.Label(
            text_frame,
            text="Transform your text into natural, professional speech",
            font=('SF Pro Display', 13),
            bg=self.colors['bg'],
            fg=self.colors['text_secondary']
        ).pack(anchor='w')
        
    def create_glass_card(self, parent, height=None):
        """Create a glassmorphism-style card"""
        card = tk.Frame(parent, bg=self.colors['card_bg'], relief='flat', bd=0)
        if height:
            card.pack(fill='x', pady=(0, 15))
            card.config(height=height)
            card.pack_propagate(False)
        else:
            card.pack(fill='both', expand=True, pady=(0, 15))
        
        return card
        
    def create_card_header(self, parent, icon, title, subtitle=None):
        """Create a styled card header"""
        header = tk.Frame(parent, bg=self.colors['card_bg'])
        header.pack(fill='x', padx=20, pady=(18, 12))
        
        # Icon + Title
        title_row = tk.Frame(header, bg=self.colors['card_bg'])
        title_row.pack(fill='x')
        
        tk.Label(
            title_row,
            text=icon,
            font=('SF Pro Display', 18),
            bg=self.colors['card_bg']
        ).pack(side='left', padx=(0, 10))
        
        tk.Label(
            title_row,
            text=title,
            font=('SF Pro Display', 15, 'bold'),
            bg=self.colors['card_bg'],
            fg=self.colors['text_primary']
        ).pack(side='left')
        
        if subtitle:
            tk.Label(
                header,
                text=subtitle,
                font=('SF Pro Display', 10),
                bg=self.colors['card_bg'],
                fg=self.colors['text_muted']
            ).pack(anchor='w', pady=(4, 0))
        
        return header
        
    def create_text_editor_card(self, parent):
        card = self.create_glass_card(parent)
        
        self.create_card_header(
            card,
            "✍️",
            "Script Editor",
            "Write or paste your content here"
        )
        
        content = tk.Frame(card, bg=self.colors['card_bg'])
        content.pack(fill='both', expand=True, padx=20, pady=(0, 20))
        
        # Toolbar
        toolbar = tk.Frame(content, bg=self.colors['input_bg'])
        toolbar.pack(fill='x', pady=(0, 10))
        
        # Character counter
        self.char_label = tk.Label(
            toolbar,
            text="0 characters • 0 words",
            font=('SF Pro Display', 10),
            bg=self.colors['input_bg'],
            fg=self.colors['text_muted'],
            pady=8,
            padx=15
        )
        self.char_label.pack(side='left')
        
        # Clear button
        clear_btn = tk.Button(
            toolbar,
            text="🗑️ Clear",
            font=('SF Pro Display', 10),
            bg=self.colors['input_bg'],
            fg=self.colors['text_secondary'],
            activebackground=self.colors['danger'],
            activeforeground='white',
            relief='flat',
            bd=0,
            padx=12,
            pady=6,
            cursor='hand2',
            command=self.clear_text
        )
        clear_btn.pack(side='right', padx=8)
        
        # Text editor
        editor_frame = tk.Frame(content, bg=self.colors['input_bg'])
        editor_frame.pack(fill='both', expand=True)
        
        self.text_input = scrolledtext.ScrolledText(
            editor_frame,
            wrap=tk.WORD,
            font=('SF Pro Text', 13),
            bg=self.colors['input_bg'],
            fg=self.colors['text_primary'],
            insertbackground=self.colors['accent_primary'],
            selectbackground=self.colors['accent_primary'],
            selectforeground='white',
            relief='flat',
            bd=0,
            padx=18,
            pady=18,
            spacing1=4,
            spacing3=4
        )
        self.text_input.pack(fill='both', expand=True)
        self.text_input.bind('<KeyRelease>', self.update_char_count)
        
        # Placeholder
        placeholder = "Start typing or paste your text here...\n\nTips:\n• Use natural punctuation for better pacing\n• Break long content into paragraphs\n• Include emphasis with ALL CAPS (use sparingly)"
        self.text_input.insert('1.0', placeholder)
        self.text_input.config(fg=self.colors['text_muted'])
        
        def on_focus_in(e):
            if self.text_input.get('1.0', 'end-1c') == placeholder:
                self.text_input.delete('1.0', tk.END)
                self.text_input.config(fg=self.colors['text_primary'])
                
        def on_focus_out(e):
            if not self.text_input.get('1.0', 'end-1c').strip():
                self.text_input.insert('1.0', placeholder)
                self.text_input.config(fg=self.colors['text_muted'])
                
        self.text_input.bind('<FocusIn>', on_focus_in)
        self.text_input.bind('<FocusOut>', on_focus_out)
        
    def create_voice_selector_card(self, parent):
        card = self.create_glass_card(parent, height=180)
        
        self.create_card_header(card, "🎤", "Voice Selection")
        
        content = tk.Frame(card, bg=self.colors['card_bg'])
        content.pack(fill='both', expand=True, padx=20, pady=(0, 18))
        
        # Voice dropdown with custom style
        tk.Label(
            content,
            text="Choose a voice",
            font=('SF Pro Display', 10),
            bg=self.colors['card_bg'],
            fg=self.colors['text_muted']
        ).pack(anchor='w', pady=(0, 6))
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure(
            'Premium.TCombobox',
            fieldbackground=self.colors['input_bg'],
            background=self.colors['input_bg'],
            foreground=self.colors['text_primary'],
            arrowcolor=self.colors['text_secondary'],
            borderwidth=0,
            relief='flat'
        )
        
        self.voice_var = tk.StringVar(value=list(self.voices.keys())[0])
        voice_combo = ttk.Combobox(
            content,
            textvariable=self.voice_var,
            values=list(self.voices.keys()),
            state='readonly',
            font=('SF Pro Display', 12),
            style='Premium.TCombobox'
        )
        voice_combo.pack(fill='x', ipady=8)
        
    def create_presets_card(self, parent):
        card = self.create_glass_card(parent, height=260)
        
        self.create_card_header(card, "⚡", "Quick Presets", "One-click voice styles")
        
        content = tk.Frame(card, bg=self.colors['card_bg'])
        content.pack(fill='both', expand=True, padx=20, pady=(0, 18))
        
        # Create preset buttons in grid
        row = 0
        col = 0
        for preset_name, preset_data in self.presets.items():
            preset_btn = tk.Frame(content, bg=self.colors['input_bg'], cursor='hand2')
            preset_btn.grid(row=row, column=col, padx=4, pady=4, sticky='nsew')
            
            # Icon
            tk.Label(
                preset_btn,
                text=preset_name.split()[0],
                font=('SF Pro Display', 20),
                bg=self.colors['input_bg']
            ).pack(pady=(10, 2))
            
            # Name
            tk.Label(
                preset_btn,
                text=' '.join(preset_name.split()[1:]),
                font=('SF Pro Display', 10, 'bold'),
                bg=self.colors['input_bg'],
                fg=self.colors['text_primary']
            ).pack()
            
            # Description
            tk.Label(
                preset_btn,
                text=preset_data['desc'],
                font=('SF Pro Display', 8),
                bg=self.colors['input_bg'],
                fg=self.colors['text_muted'],
                wraplength=100
            ).pack(pady=(2, 10))
            
            # Bind click
            for widget in preset_btn.winfo_children():
                widget.bind('<Button-1>', lambda e, p=preset_name: self.apply_preset(p))
            preset_btn.bind('<Button-1>', lambda e, p=preset_name: self.apply_preset(p))
            
            # Hover effect
            def on_enter(e, btn=preset_btn):
                btn.config(bg=self.colors['card_hover'])
                for child in btn.winfo_children():
                    child.config(bg=self.colors['card_hover'])
            
            def on_leave(e, btn=preset_btn):
                btn.config(bg=self.colors['input_bg'])
                for child in btn.winfo_children():
                    child.config(bg=self.colors['input_bg'])
            
            preset_btn.bind('<Enter>', on_enter)
            preset_btn.bind('<Leave>', on_leave)
            
            col += 1
            if col > 1:
                col = 0
                row += 1
        
        content.columnconfigure(0, weight=1)
        content.columnconfigure(1, weight=1)
        
    def create_controls_card(self, parent):
        card = self.create_glass_card(parent, height=200)
        
        self.create_card_header(card, "🎛️", "Voice Controls", "Fine-tune speed and pitch")
        
        content = tk.Frame(card, bg=self.colors['card_bg'])
        content.pack(fill='both', expand=True, padx=20, pady=(0, 18))
        
        # Speed slider
        self.create_premium_slider(content, "⚡ Speed", -50, 50, 0, '%', 'rate')
        
        # Pitch slider
        self.create_premium_slider(content, "🎵 Pitch", -20, 20, 0, 'Hz', 'pitch')
        
    def create_premium_slider(self, parent, label, min_val, max_val, default, unit, var_name):
        container = tk.Frame(parent, bg=self.colors['card_bg'])
        container.pack(fill='x', pady=(0, 20))
        
        # Header
        header = tk.Frame(container, bg=self.colors['card_bg'])
        header.pack(fill='x', pady=(0, 8))
        
        tk.Label(
            header,
            text=label,
            font=('SF Pro Display', 11),
            bg=self.colors['card_bg'],
            fg=self.colors['text_secondary']
        ).pack(side='left')
        
        value_label = tk.Label(
            header,
            text=f"{default}{unit}",
            font=('SF Pro Display', 11, 'bold'),
            bg=self.colors['card_bg'],
            fg=self.colors['accent_primary']
        )
        value_label.pack(side='right')
        
        # Slider
        slider = tk.Scale(
            container,
            from_=min_val,
            to=max_val,
            orient='horizontal',
            bg=self.colors['card_bg'],
            fg=self.colors['text_primary'],
            highlightthickness=0,
            troughcolor=self.colors['input_bg'],
            activebackground=self.colors['accent_primary'],
            sliderrelief='flat',
            bd=0,
            showvalue=False,
            font=('SF Pro Display', 10),
            length=280
        )
        slider.set(default)
        slider.pack(fill='x')
        
        def update_value(val):
            val = int(float(val))
            value_label.config(text=f"{val}{unit}")
            if val > 0:
                value_label.config(fg=self.colors['success'])
            elif val < 0:
                value_label.config(fg=self.colors['warning'])
            else:
                value_label.config(fg=self.colors['text_secondary'])
        
        slider.config(command=update_value)
        setattr(self, f'{var_name}_slider', slider)
        
    def create_action_buttons(self, parent):
        container = tk.Frame(parent, bg=self.colors['bg'])
        container.pack(fill='x', pady=(5, 0))
        
        # Generate Button (Primary CTA)
        self.generate_btn = tk.Button(
            container,
            text="🎙️  Generate Speech",
            font=('SF Pro Display', 14, 'bold'),
            bg=self.colors['accent_primary'],
            fg='white',
            activebackground=self.colors['accent_secondary'],
            activeforeground='white',
            relief='flat',
            bd=0,
            padx=25,
            pady=16,
            cursor='hand2',
            command=self.start_generation
        )
        self.generate_btn.pack(fill='x', pady=(0, 10))
        
        # Secondary actions row
        actions_row = tk.Frame(container, bg=self.colors['bg'])
        actions_row.pack(fill='x')
        
        # Save As button
        save_btn = tk.Button(
            actions_row,
            text="💾 Save As",
            font=('SF Pro Display', 11),
            bg=self.colors['card_bg'],
            fg=self.colors['text_primary'],
            activebackground=self.colors['card_hover'],
            activeforeground=self.colors['text_primary'],
            relief='flat',
            bd=0,
            padx=20,
            pady=12,
            cursor='hand2',
            command=self.save_as_dialog
        )
        save_btn.pack(side='left', fill='x', expand=True, padx=(0, 5))
        
        # Load File button
        load_btn = tk.Button(
            actions_row,
            text="📁 Load",
            font=('SF Pro Display', 11),
            bg=self.colors['card_bg'],
            fg=self.colors['text_primary'],
            activebackground=self.colors['card_hover'],
            activeforeground=self.colors['text_primary'],
            relief='flat',
            bd=0,
            padx=20,
            pady=12,
            cursor='hand2',
            command=self.load_file
        )
        load_btn.pack(side='right', fill='x', expand=True, padx=(5, 0))
        
    def create_status_bar(self, parent):
        bar = tk.Frame(parent, bg=self.colors['card_bg'], height=50)
        bar.pack(fill='x')
        bar.pack_propagate(False)
        
        content = tk.Frame(bar, bg=self.colors['card_bg'])
        content.pack(fill='both', expand=True, padx=25)
        
        # Status indicator
        self.status_dot = tk.Label(
            content,
            text="●",
            font=('SF Pro Display', 14),
            bg=self.colors['card_bg'],
            fg=self.colors['success']
        )
        self.status_dot.pack(side='left', padx=(0, 8))
        
        self.status_label = tk.Label(
            content,
            text="Ready to generate",
            font=('SF Pro Display', 11),
            bg=self.colors['card_bg'],
            fg=self.colors['text_secondary']
        )
        self.status_label.pack(side='left')
        
        # Output file info
        self.file_label = tk.Label(
            content,
            text="📁 output.mp3",
            font=('SF Pro Display', 10),
            bg=self.colors['card_bg'],
            fg=self.colors['text_muted']
        )
        self.file_label.pack(side='right')
        
    # Event Handlers
    def update_char_count(self, event=None):
        text = self.text_input.get('1.0', 'end-1c')
        char_count = len(text)
        word_count = len(text.split())
        self.char_label.config(text=f"{char_count} characters • {word_count} words")
        
    def clear_text(self):
        self.text_input.delete('1.0', tk.END)
        self.update_char_count()
        
    def load_file(self):
        filename = filedialog.askopenfilename(
            title="Load Text File",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.text_input.delete('1.0', tk.END)
                self.text_input.insert('1.0', content)
                self.text_input.config(fg=self.colors['text_primary'])
                self.update_status(f"Loaded: {os.path.basename(filename)}", self.colors['success'])
            except Exception as e:
                messagebox.showerror("Load Error", f"Failed to load file:\n{e}")
                
    def save_as_dialog(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".mp3",
            filetypes=[("MP3 Files", "*.mp3"), ("All Files", "*.*")],
            title="Save Audio As"
        )
        if filename:
            self.output_file = filename
            self.file_label.config(text=f"📁 {os.path.basename(filename)}")
            self.update_status(f"Will save as: {os.path.basename(filename)}", self.colors['text_secondary'])
            
    def apply_preset(self, preset_name):
        preset = self.presets[preset_name]
        
        # Find matching voice
        for display_name, voice_id in self.voices.items():
            if voice_id == preset['voice']:
                self.voice_var.set(display_name)
                break
        
        self.rate_slider.set(preset['rate'])
        self.pitch_slider.set(preset['pitch'])
        
        self.update_status(f"Applied preset: {preset_name}", self.colors['accent_primary'])
        
    def update_status(self, message, color):
        self.status_label.config(text=message, fg=color)
        self.status_dot.config(fg=color)
        
    def start_generation(self):
        text = self.text_input.get('1.0', 'end-1c').strip()
        
        if not text or 'Start typing' in text:
            messagebox.showwarning("No Content", "Please enter some text to convert to speech.")
            return
        
        self.generate_btn.config(
            state='disabled',
            text="⏳ Generating...",
            bg=self.colors['text_muted']
        )
        self.update_status("Generating audio...", self.colors['warning'])
        
        voice_display = self.voice_var.get()
        voice = self.voices[voice_display]
        rate = self.format_rate(self.rate_slider.get())
        pitch = self.format_pitch(self.pitch_slider.get())
        
        thread = threading.Thread(
            target=self.run_generation,
            args=(text, voice, rate, pitch),
            daemon=True
        )
        thread.start()
        
    def run_generation(self, text, voice, rate, pitch):
        try:
            asyncio.run(self.generate_audio(text, voice, rate, pitch))
            self.root.after(0, self.generation_complete)
        except Exception as e:
            self.root.after(0, lambda: self.generation_failed(str(e)))
            
    async def generate_audio(self, text, voice, rate, pitch):
        communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await communicate.save(self.output_file)
        
    def generation_complete(self):
        self.generate_btn.config(
            state='normal',
            text="🎙️  Generate Speech",
            bg=self.colors['accent_primary']
        )
        self.update_status("✓ Audio generated successfully!", self.colors['success'])
        
        # Play audio
        if os.path.exists(self.output_file):
            subprocess.run(['afplay', self.output_file], check=False)
            
    def generation_failed(self, error):
        self.generate_btn.config(
            state='normal',
            text="🎙️  Generate Speech",
            bg=self.colors['accent_primary']
        )
        self.update_status(f"Generation failed: {error}", self.colors['danger'])
        messagebox.showerror("Error", f"Failed to generate audio:\n{error}")
        
    def format_rate(self, value):
        return f"+{int(value)}%" if value >= 0 else f"{int(value)}%"
        
    def format_pitch(self, value):
        return f"+{int(value)}Hz" if value >= 0 else f"{int(value)}Hz"

# For standalone testing
if __name__ == "__main__":
    root = tk.Tk()
    app = PremiumTTSApp(root)
    root.mainloop()