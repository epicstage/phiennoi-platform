'use client';

import React from 'react';
import KBeautyExpoTemplate from './KBeautyExpoTemplate';
import OffshoreTechTemplate from './OffshoreTechTemplate';
import GeneralMeetingTemplate from './GeneralMeetingTemplate';

export { KBeautyExpoTemplate, OffshoreTechTemplate, GeneralMeetingTemplate };

// Template data type definitions
export type KBeautyData = React.ComponentProps<typeof KBeautyExpoTemplate>['data'];
export type OffshoreTechData = React.ComponentProps<typeof OffshoreTechTemplate>['data'];
export type GeneralMeetingData = React.ComponentProps<typeof GeneralMeetingTemplate>['data'];

// Template renderer component
interface TemplateRendererProps {
  templateId: string;
  formData: Record<string, string>;
  mode?: 'preview' | 'print';
}

export function TemplateRenderer({ templateId, formData, mode = 'preview' }: TemplateRendererProps) {
  // Convert flat form data to template-specific data structure
  const convertFormData = () => {
    switch (templateId) {
      case 'kbeauty-expo': {
        // Parse buyer data from numbered fields
        const buyers = [];
        let buyerIndex = 1;
        while (formData[`buyer${buyerIndex}_company`] || buyerIndex === 1) {
          if (buyerIndex > 5) break; // Max 5 buyers
          buyers.push({
            companyName: formData[`buyer${buyerIndex}_company`] || '',
            contactPerson: formData[`buyer${buyerIndex}_contact`] || '',
            position: formData[`buyer${buyerIndex}_position`] || '',
            contactPoint: formData[`buyer${buyerIndex}_phone`] || formData[`buyer${buyerIndex}_email`] || '',
            time: formData[`buyer${buyerIndex}_time`] || '',
            items: formData[`buyer${buyerIndex}_items`] || formData['consult_items'] || '',
            consultType: {
              priceConsult: formData[`buyer${buyerIndex}_price_consult`] === 'true' || formData['price_consult'] === 'true',
              sampleRequest: formData[`buyer${buyerIndex}_sample_request`] === 'true' || formData['sample_request'] === 'true',
              agentConsult: formData[`buyer${buyerIndex}_agent_consult`] === 'true' || formData['agent_consult'] === 'true',
              qualityConsult: formData[`buyer${buyerIndex}_quality_consult`] === 'true' || formData['quality_consult'] === 'true',
              otherConsult: formData[`buyer${buyerIndex}_other_consult`] === 'true' || formData['other_consult'] === 'true',
              marketResearch: formData[`buyer${buyerIndex}_market_research`] === 'true' || formData['market_research'] === 'true',
              regulationConsult: formData[`buyer${buyerIndex}_regulation_consult`] === 'true' || formData['regulation_consult'] === 'true',
            },
            result: {
              contractSigned: formData[`buyer${buyerIndex}_contract`] === 'true' || formData['contract_signed'] === 'true',
              sampleProvided: formData[`buyer${buyerIndex}_sample_provided`] === 'true' || formData['sample_provided'] === 'true',
              catalogProvided: formData[`buyer${buyerIndex}_catalog`] === 'true' || formData['catalog_provided'] === 'true',
              revisit: formData[`buyer${buyerIndex}_revisit`] === 'true' || formData['revisit'] === 'true',
              noResult: formData[`buyer${buyerIndex}_no_result`] === 'true' || formData['no_result'] === 'true',
            },
            rating: {
              interest: parseInt(formData[`buyer${buyerIndex}_interest`] || formData['interest_rating'] || '3', 10),
              purchase: parseInt(formData[`buyer${buyerIndex}_purchase`] || formData['purchase_rating'] || '3', 10),
            },
            exportAmount: formData[`buyer${buyerIndex}_export_amount`] || formData['export_amount'] || '',
            currency: (formData[`buyer${buyerIndex}_currency`] || formData['currency'] || 'USD') as 'USD' | 'VND',
            notes: formData[`buyer${buyerIndex}_notes`] || formData['notes'] || '',
          });
          buyerIndex++;
        }

        // Ensure at least one buyer entry
        if (buyers.length === 0) {
          buyers.push({
            companyName: formData['buyer_company'] || '',
            contactPerson: formData['buyer_contact'] || '',
            position: formData['buyer_position'] || '',
            contactPoint: formData['buyer_phone'] || '',
            time: formData['consult_time'] || '',
            items: formData['consult_items'] || '',
            consultType: {
              priceConsult: formData['price_consult'] === 'true',
              sampleRequest: formData['sample_request'] === 'true',
              agentConsult: formData['agent_consult'] === 'true',
              qualityConsult: formData['quality_consult'] === 'true',
              otherConsult: formData['other_consult'] === 'true',
              marketResearch: formData['market_research'] === 'true',
              regulationConsult: formData['regulation_consult'] === 'true',
            },
            result: {
              contractSigned: formData['contract_signed'] === 'true',
              sampleProvided: formData['sample_provided'] === 'true',
              catalogProvided: formData['catalog_provided'] === 'true',
              revisit: formData['revisit'] === 'true',
              noResult: formData['no_result'] === 'true',
            },
            rating: {
              interest: parseInt(formData['interest_rating'] || '3', 10),
              purchase: parseInt(formData['purchase_rating'] || '3', 10),
            },
            exportAmount: formData['export_amount'] || '',
            currency: (formData['currency'] || 'USD') as 'USD' | 'VND',
            notes: formData['notes'] || '',
          });
        }

        return {
          date: formData['date'] || new Date().toISOString().split('T')[0],
          koreanCompany: formData['korean_company'] || '',
          boothNo: formData['booth_no'] || '',
          staff: formData['staff'] || formData['interpreter'] || '',
          interpreter: formData['interpreter'] || '',
          buyers,
        };
      }

      case 'offshore-tech': {
        const meetings = [];
        let meetingIndex = 1;
        while (formData[`meeting${meetingIndex}_kr_company`] || meetingIndex === 1) {
          if (meetingIndex > 10) break;
          meetings.push({
            time: formData[`meeting${meetingIndex}_time`] || formData['meeting_time'] || '',
            koreanCompany: {
              companyName: formData[`meeting${meetingIndex}_kr_company`] || formData['kr_company'] || '',
              contactPerson: formData[`meeting${meetingIndex}_kr_contact`] || formData['kr_contact'] || '',
              position: formData[`meeting${meetingIndex}_kr_position`] || formData['kr_position'] || '',
              phone: formData[`meeting${meetingIndex}_kr_phone`] || formData['kr_phone'] || '',
              email: formData[`meeting${meetingIndex}_kr_email`] || formData['kr_email'] || '',
              address: formData[`meeting${meetingIndex}_kr_address`] || '',
              industry: formData[`meeting${meetingIndex}_kr_industry`] || formData['kr_industry'] || '',
              employees: formData[`meeting${meetingIndex}_kr_employees`] || '',
              revenue: formData[`meeting${meetingIndex}_kr_revenue`] || '',
            },
            vietnameseCompany: {
              companyName: formData[`meeting${meetingIndex}_vn_company`] || formData['vn_company'] || '',
              contactPerson: formData[`meeting${meetingIndex}_vn_contact`] || formData['vn_contact'] || '',
              position: formData[`meeting${meetingIndex}_vn_position`] || formData['vn_position'] || '',
              phone: formData[`meeting${meetingIndex}_vn_phone`] || formData['vn_phone'] || '',
              email: formData[`meeting${meetingIndex}_vn_email`] || formData['vn_email'] || '',
              address: formData[`meeting${meetingIndex}_vn_address`] || '',
              industry: formData[`meeting${meetingIndex}_vn_industry`] || formData['vn_industry'] || '',
              employees: formData[`meeting${meetingIndex}_vn_employees`] || '',
              revenue: formData[`meeting${meetingIndex}_vn_revenue`] || '',
            },
            meetingPurpose: {
              partnership: formData[`meeting${meetingIndex}_purpose_partnership`] === 'true' || formData['purpose_partnership'] === 'true',
              investment: formData[`meeting${meetingIndex}_purpose_investment`] === 'true' || formData['purpose_investment'] === 'true',
              techTransfer: formData[`meeting${meetingIndex}_purpose_tech`] === 'true' || formData['purpose_tech'] === 'true',
              outsourcing: formData[`meeting${meetingIndex}_purpose_outsourcing`] === 'true' || formData['purpose_outsourcing'] === 'true',
              marketResearch: formData[`meeting${meetingIndex}_purpose_market`] === 'true' || formData['purpose_market'] === 'true',
              other: formData[`meeting${meetingIndex}_purpose_other`] === 'true' || formData['purpose_other'] === 'true',
            },
            discussionPoints: formData[`meeting${meetingIndex}_discussion`] || formData['discussion_points'] || '',
            actionItems: formData[`meeting${meetingIndex}_actions`] || formData['action_items'] || '',
            followUp: formData[`meeting${meetingIndex}_followup`] || formData['follow_up'] || '',
            rating: {
              potential: parseInt(formData[`meeting${meetingIndex}_potential`] || formData['potential_rating'] || '3', 10),
              urgency: parseInt(formData[`meeting${meetingIndex}_urgency`] || formData['urgency_rating'] || '3', 10),
            },
            notes: formData[`meeting${meetingIndex}_notes`] || formData['notes'] || '',
          });
          meetingIndex++;
        }

        return {
          eventName: formData['event_name'] || '2025 한-베 오프쇼어 테크 커넥트',
          date: formData['date'] || new Date().toISOString().split('T')[0],
          venue: formData['venue'] || '',
          interpreter: formData['interpreter'] || '',
          meetings,
        };
      }

      case 'general-meeting':
      default: {
        return {
          date: formData['date'] || new Date().toISOString().split('T')[0],
          venue: formData['venue'] || '',
          eventName: formData['event_name'] || '',
          interpreter: formData['interpreter'] || '',
          koreanParty: {
            company: formData['kr_company'] || '',
            participants: formData['kr_participants'] || '',
          },
          vietnameseParty: {
            company: formData['vn_company'] || '',
            participants: formData['vn_participants'] || '',
          },
          agenda: formData['agenda'] || '',
          discussion: formData['discussion'] || '',
          decisions: formData['decisions'] || '',
          actionItems: formData['action_items'] || '',
          nextMeeting: formData['next_meeting'] || '',
          notes: formData['notes'] || '',
        };
      }
    }
  };

  const templateData = convertFormData();

  switch (templateId) {
    case 'kbeauty-expo':
      return <KBeautyExpoTemplate data={templateData as KBeautyData} mode={mode} />;
    case 'offshore-tech':
      return <OffshoreTechTemplate data={templateData as OffshoreTechData} mode={mode} />;
    case 'general-meeting':
    default:
      return <GeneralMeetingTemplate data={templateData as GeneralMeetingData} mode={mode} />;
  }
}

// Empty template data for preview
export function getEmptyTemplateData(templateId: string): Record<string, string> {
  switch (templateId) {
    case 'kbeauty-expo':
      return {
        date: new Date().toISOString().split('T')[0],
        korean_company: '(회사명)',
        booth_no: '(부스번호)',
        staff: '(담당자)',
        interpreter: '(통역사)',
        buyer_company: '(바이어 회사명)',
        buyer_contact: '(담당자)',
        buyer_position: '(직책)',
        buyer_phone: '(연락처)',
        consult_time: '10:00',
        consult_items: '(상담 아이템)',
        interest_rating: '3',
        purchase_rating: '3',
        export_amount: '',
        currency: 'USD',
        notes: '',
      };
    case 'offshore-tech':
      return {
        event_name: '2025 한-베 오프쇼어 테크 커넥트',
        date: new Date().toISOString().split('T')[0],
        venue: '(장소)',
        interpreter: '(통역사)',
        meeting_time: '10:00',
        kr_company: '(한국 회사명)',
        kr_contact: '(담당자)',
        kr_position: '(직책)',
        kr_phone: '(연락처)',
        kr_email: '(이메일)',
        kr_industry: '(업종)',
        vn_company: '(베트남 회사명)',
        vn_contact: '(담당자)',
        vn_position: '(직책)',
        vn_phone: '(연락처)',
        vn_email: '(이메일)',
        vn_industry: '(업종)',
        discussion_points: '(논의 사항)',
        action_items: '(후속 조치)',
        potential_rating: '3',
        urgency_rating: '3',
        notes: '',
      };
    case 'general-meeting':
    default:
      return {
        date: new Date().toISOString().split('T')[0],
        venue: '(장소)',
        event_name: '(행사명)',
        interpreter: '(통역사)',
        kr_company: '(한국 회사명)',
        kr_participants: '(참석자)',
        vn_company: '(베트남 회사명)',
        vn_participants: '(참석자)',
        agenda: '(안건)',
        discussion: '(논의 내용)',
        decisions: '(결정 사항)',
        action_items: '(액션 아이템)',
        next_meeting: '(차기 일정)',
        notes: '',
      };
  }
}
