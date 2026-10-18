import io
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


def draw_certificate_background(canvas, doc):
    """
    Draws the certificate background tint, decorative green borders, corner ornaments,
    and accent bands before flowable content is rendered.
    This guarantees all text and metadata are drawn on top of the background.
    """
    canvas.saveState()
    width, height = doc.pagesize

    # 1. Background soft tint (off-white / cream green tint #FAFCF9)
    canvas.setFillColor(colors.HexColor('#FAFCF9'))
    canvas.rect(0, 0, width, height, fill=1, stroke=0)

    # 2. Outer decorative border (Dark Green #166534, 3pt)
    canvas.setStrokeColor(colors.HexColor('#166534'))
    canvas.setLineWidth(3.0)
    canvas.rect(24, 24, width - 48, height - 48)

    # Inner decorative border (Emerald Green #16A34A, 1pt)
    canvas.setStrokeColor(colors.HexColor('#16A34A'))
    canvas.setLineWidth(1.0)
    canvas.rect(30, 30, width - 60, height - 60)

    # 3. Corner accents (Solid Emerald #15803D squares)
    accent_color = colors.HexColor('#15803D')
    canvas.setFillColor(accent_color)
    corner_size = 18

    # Top-left corner box
    canvas.rect(30, height - 30 - corner_size, corner_size, corner_size, fill=1, stroke=0)
    # Top-right corner box
    canvas.rect(width - 30 - corner_size, height - 30 - corner_size, corner_size, corner_size, fill=1, stroke=0)
    # Bottom-left corner box
    canvas.rect(30, 30, corner_size, corner_size, fill=1, stroke=0)
    # Bottom-right corner box
    canvas.rect(width - 30 - corner_size, 30, corner_size, corner_size, fill=1, stroke=0)

    # 4. Subtle decorative horizontal accent bands
    canvas.setFillColor(colors.HexColor('#DCFCE7'))
    canvas.rect(40, height - 52, width - 80, 2, fill=1, stroke=0)
    canvas.rect(40, 52, width - 80, 2, fill=1, stroke=0)

    canvas.restoreState()


def generate_certificate_pdf(certificate):
    """
    Generates a professional A4 landscape vector PDF for the given Certificate model instance.
    Guarantees:
      - Authenticated candidate full name
      - Unique Certificate ID
      - Exam / Course Specialization title
      - Issue Date
      - "Platform Representative" signature label
      - STRICTLY NO marks, percentages, pass/fail wording, or external institution seals.
      - Vector text layered on top of background.
    """
    buffer = io.BytesIO()

    # A4 Landscape dimensions: 841.89 x 595.27 points
    doc = SimpleDocTemplate(
        buffer,
        pagesize=landscape(A4),
        leftMargin=50,
        rightMargin=50,
        topMargin=45,
        bottomMargin=45
    )

    styles = getSampleStyleSheet()

    # Custom typography styles tailored for A4 landscape
    brand_style = ParagraphStyle(
        'CertBrand',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#166534'),
        alignment=1,  # Center
        spaceAfter=3,
    )

    sub_brand_style = ParagraphStyle(
        'CertSubBrand',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor('#15803D'),
        alignment=1,
        spaceAfter=14,
    )

    heading_style = ParagraphStyle(
        'CertHeading',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=28,
        leading=32,
        textColor=colors.HexColor('#172B21'),
        alignment=1,
        spaceAfter=5,
    )

    ribbon_style = ParagraphStyle(
        'CertRibbon',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#16A34A'),
        alignment=1,
        spaceAfter=14,
    )

    presented_style = ParagraphStyle(
        'CertPresented',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor('#64748B'),
        alignment=1,
        spaceAfter=8,
    )

    name_style = ParagraphStyle(
        'CertName',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=25,
        leading=29,
        textColor=colors.HexColor('#166534'),
        alignment=1,
        spaceAfter=10,
    )

    body_desc_style = ParagraphStyle(
        'CertDesc',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10.5,
        leading=15,
        textColor=colors.HexColor('#334155'),
        alignment=1,
        spaceAfter=8,
    )

    exam_title_style = ParagraphStyle(
        'CertExamTitle',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#172B21'),
        alignment=1,
        spaceAfter=18,
    )

    meta_label_style = ParagraphStyle(
        'CertMetaLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#64748B'),
        alignment=0,
    )

    meta_val_style = ParagraphStyle(
        'CertMetaVal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#0F172A'),
        alignment=0,
    )

    sig_name_style = ParagraphStyle(
        'CertSigName',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=16,
        leading=18,
        textColor=colors.HexColor('#166534'),
        alignment=2,  # Right
    )

    sig_title_style = ParagraphStyle(
        'CertSigTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#334155'),
        alignment=2,  # Right
    )

    sig_subtitle_style = ParagraphStyle(
        'CertSigSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor('#64748B'),
        alignment=2,  # Right
    )

    story = []

    # Top spacing
    story.append(Spacer(1, 10))

    # Top Brand / Header
    story.append(Paragraph("CODING CHALLENGE PLATFORM", brand_style))
    story.append(Paragraph("OFFICIAL ASSESSMENT &amp; CERTIFICATION AUTHORITY", sub_brand_style))

    # Certificate Title & Ribbon
    story.append(Paragraph("CERTIFICATE OF COMPLETION", heading_style))
    story.append(Paragraph("&mdash;&mdash; VERIFIED TECHNICAL CREDENTIAL &mdash;&mdash;", ribbon_style))

    story.append(Paragraph("THIS CERTIFICATE IS PROUDLY CONFERRED TO", presented_style))

    # Candidate Name
    candidate_display_name = (
        certificate.candidate_name
        or (certificate.user.get_full_name() if hasattr(certificate.user, 'get_full_name') and certificate.user.get_full_name() else '')
        or certificate.user.username
        or "Candidate"
    )
    story.append(Paragraph(candidate_display_name.upper(), name_style))

    # Narrative Statement
    story.append(
        Paragraph(
            "for successfully completing all required theoretical evaluations, hands-on programming challenges, "
            "and demonstrating recognized competence in",
            body_desc_style
        )
    )

    # Exam / Specialization Name
    exam_title = certificate.exam.title if certificate.exam else "Certification Assessment"
    story.append(Paragraph(exam_title, exam_title_style))

    story.append(Spacer(1, 12))

    # Footer Table: Left column = Certificate ID & Date; Right column = Signature & Title
    if hasattr(certificate.issue_date, 'strftime'):
        issue_date_str = certificate.issue_date.strftime("%B %d, %Y")
    else:
        issue_date_str = str(certificate.issue_date)

    left_cell = [
        Paragraph("CERTIFICATE ID", meta_label_style),
        Paragraph(f"<b>{certificate.certificate_id}</b>", meta_val_style),
        Spacer(1, 4),
        Paragraph("DATE OF ISSUANCE", meta_label_style),
        Paragraph(issue_date_str, meta_val_style),
        Spacer(1, 4),
        Paragraph("SECURITY STATUS", meta_label_style),
        Paragraph("Digitally Verified &amp; Validated", meta_val_style),
    ]

    signatory_title = certificate.signatory_title or "Platform Representative"
    right_cell = [
        Paragraph("C. C. Platform", sig_name_style),
        Spacer(1, 3),
        Paragraph(signatory_title, sig_title_style),
        Paragraph("Coding Challenge Platform Certification Board", sig_subtitle_style),
    ]

    footer_data = [[left_cell, '', right_cell]]
    # Total width: 240 + 260 + 240 = 740 pt (fits within 841.89 - 100 = 741.89 pt)
    footer_table = Table(
        footer_data,
        colWidths=[240, 260, 240]
    )
    footer_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))

    story.append(footer_table)

    # Build document with onFirstPage callback to paint background before flowables
    doc.build(story, onFirstPage=draw_certificate_background)
    buffer.seek(0)
    return buffer
