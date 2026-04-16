import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace the old cta-form styles
old_styles = '''        .cta-form {
            max-width: 500px;
            margin: 0 auto;
            display: flex;
            gap: 12px;
        }

        .cta-form input {
            flex: 1;
            padding: 18px 24px;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-family: 'Inter', sans-serif;
            background: rgba(255, 255, 255, 0.1);
            color: var(--white);
            border: 1px solid rgba(255, 255, 255, 0.2);
            transition: all 0.3s ease;
        }'''

new_styles = '''        .cta-form {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
            max-width: 700px;
            margin: 0 auto;
            padding: 30px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            border: 1px solid rgba(201, 169, 97, 0.3);
        }

        .cta-form input {
            width: 100%;
            padding: 14px 18px;
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 6px;
            font-size: 15px;
            background: rgba(255, 255, 255, 0.08);
            color: var(--white);
        }'''

content = content.replace(old_styles, new_styles)

# Add button full width
old_button = '''        .cta-form button {
            padding: 18px 36px;
            background: var(--gold);
            color: var(--charcoal);
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 700;
            font-family: 'Montserrat', sans-serif;
            cursor: pointer;
            transition: all 0.3s ease;
            white-space: nowrap;
        }'''

new_button = '''        .cta-form button {
            grid-column: span 2;
            padding: 16px 32px;
            background: var(--gold);
            color: var(--charcoal);
            border: none;
            border-radius: 6px;
            font-size: 16px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s ease;
            margin-top: 10px;
        }'''

content = content.replace(old_button, new_button)

# Add responsive styles
old_media = '''        @media (max-width: 768px) {'''

new_media = '''        .cta-form button:hover {
            background: var(--gold-light);
            transform: translateY(-2px);
        }

        @media (max-width: 600px) {
            .cta-form {
                grid-template-columns: 1fr;
            }
            .cta-form button {
                grid-column: span 1;
            }
        }

        @media (max-width: 768px) {'''

content = content.replace(old_media, new_media)

with open('index.html', 'w') as f:
    f.write(content)

print('Form styles updated!')
